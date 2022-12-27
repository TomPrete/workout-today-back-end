from django.shortcuts import redirect
from rest_framework_simplejwt.views import TokenObtainPairView
from exercises.models import User
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import os
import stripe
from mixpanel import Mixpanel

mp = Mixpanel('c9b89c7bf5d74371eaa2dbf629c20821')

stripe.api_key = 'sk_test_51LTVzmCxk3VOyNJUcsZ4S3O5C7y1p6tLcLw37L17reSYaZyIdSlUxMMKkboTgXo0sePUsYoJ5QdSEVvqiDAHJv6G00e0wdArHg'

endpoint_secret = 'whsec_ba7c25d90b4323378364b4c666d220db1656797062019a8906503f12a044e513'

development = True

FRONTEND_DOMAIN_URL = "https://app.workouttoday.co/" if development == False else 'http://localhost:3000/'

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomUserAuth(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        if request.user.is_authenticated:
            return Response({
                'username': request.user.username,
                'email': request.user.email,
                'is_premium': request.user.is_premium,
                'id': request.user.id
                })

        else:
            return Response({'message': 'user not logged in'})

def create_stripe_customer(user):
    customer = stripe.Customer.create(email=user.email)
    update_user_with_stripe_id(customer, user)
    return customer

def update_user_with_stripe_id(stripe_customer, user):
    try:
        user.stripe_id=stripe_customer.id
        user.save()
        return True
    except Exception as e:
       return False

def get_stripe_customer(user):
    try:
        customer = stripe.Customer.retrieve(user.stripe_id)
        return customer
    except Exception as e:
        return e

def get_subscription_key(subscription_type):
    if subscription_type == 'monthly':
        price_id = 'price_1M6j70Cxk3VOyNJUHyaJ4IQ5'
    else:
        price_id = 'price_1M6jJPCxk3VOyNJUwyFqanWS'
    return price_id

def find_customer_by_email(email):
    try:
        user = User.objects.get(email=email)
        return user
    except Exception as e:
        return e

def find_customer_by_stripe_id(stripe_id):
    try:
        user = User.objects.get(stripe_id=stripe_id)
        return user
    except Exception as e:
        return e

def update_user_with_stripe_customer_id(user, stripe_id):
    user.stripe_id = stripe_id
    user.save()
    return user

class SubscriptionWebhook(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        payload = request.body.decode('utf-8')
        try:
            event = stripe.Webhook.construct_event(
                    payload, sig_header, endpoint_secret
                )
        except ValueError as e:
            # Invalid payload
            return Response({'message': 'value error'}, status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            print('Invalid signature')
            return Response({'message': f"SignatureVerificationError: {e}"}, status=400)

        if event['type'] == 'customer.created':
            email = event['data']['object']['email']
            stripe_customer_id = event['data']['object']['id']
            user = find_customer_by_email(email)
            update_user_with_stripe_customer_id(user, stripe_customer_id)
        elif event['type'] == 'customer.subscription.created':
            print('customer.subscription.created: ', event['data'])
        elif event['type'] == 'invoice.payment_succeeded':
            email = event['data']['object']['customer_email']
            user = find_customer_by_email(email)
            if user.is_premium != True:
                user.is_premium = True
                user.save()
        elif event['type'] == 'payment_intent.succeeded':
            stripe_id = event['data']['object']['customer']
            user = find_customer_by_stripe_id(stripe_id)
            if user.is_premium != True:
                user.is_premium = True
                user.save()
            else:
                print("Customer already is premium")
        elif event['type'] == 'customer.subscription.deleted':
            stripe_id = event['data']['object']['customer']
            user = find_customer_by_stripe_id(stripe_id)
            if user.is_premium == True:
                user.is_premium = False
                user.save()
            else:
                print("Customer already is premium")
        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']

            # Use stored information to get an error object
            e = payment_intent['last_payment_error']

            # Use its type to choose a response
            mp.track(e['payment_method']['customer'], 'card_declined')
            if e['type'] == 'card_error':
                print("A payment error occurred: {}".format(e['message']))
            elif e['type'] == 'invalid_request':
                print("An invalid request occurred.")
            else:
                print("Another problem occurred, maybe unrelated to Stripe")



        data = {
            'message': 'subscription succeeded'
        }
        return Response(data, status=200)

class CheckoutSession(APIView):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = []

    def post(self, request, format=None):
        checkout_info = json.load(request)
        try:
            # print('checkout_info: ', checkout_info)
            if request.user.stripe_id:
                stripe_customer = get_stripe_customer(request.user)
            else:
                stripe_customer = create_stripe_customer(request.user)
            price = stripe.Price.retrieve(
                get_subscription_key(checkout_info)
            )
            # print("PRICE: ", price)
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': price.id,
                        'quantity': 1,
                    },
                ],
                # subscription_data={
                #     'trial_period_days': 7
                # },
                automatic_tax={
                    'enabled': False
                },
                mode='subscription',
                customer=stripe_customer.id,
                success_url=f"{FRONTEND_DOMAIN_URL}login" +
                '?success=true',
                cancel_url=f"{FRONTEND_DOMAIN_URL}login" + '?canceled=true',
            )
            data = {
                'stripe_url': checkout_session.url
            }
            return Response(data, status=303)
        except Exception as e:
            print("EXCEPTION: ", e)
            data = {
                'message': e
            }
            return Response(data, status=500)

class CustomerPortalSession(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        # print(request.user)
        user_info = json.load(request)
        # print("EMAIL: ", user_info)
        try:
            stripe_id = request.user.stripe_id
            customer = get_stripe_customer(request.user)
            # subscription = stripe.Subscription.list(customer=stripe_id)
            # print("SUBSCRIPTION: ", subscription)
            portal_configuration = stripe.billing_portal.Configuration.create(
                business_profile={
                    "headline": "Cactus Practice partners with Stripe for simplified billing.",
                },
                features={
                    "invoice_history": {
                        "enabled": True
                        },
                    "payment_method_update": {
                        "enabled": True
                        },
                    "subscription_cancel": {
                        "cancellation_reason": {
                            "enabled": True,
                            "options": [
                                'too_expensive',
                                'missing_features',
                                'switched_service',
                                'unused',
                                'too_complex',
                                'low_quality',
                                'other'
                                ]
                        },
                        "enabled": True,
                        "mode": "at_period_end",
                        "proration_behavior": "none"
                        },
                    "subscription_pause": {
                        "enabled": True
                        },
                    "subscription_update": {
                        "default_allowed_updates": ["price"],
                        "products": [
                            {
                                "product": "prod_MqPztshwi4bDEH",
                                "prices": ["price_1M6jJPCxk3VOyNJUwyFqanWS"]
                            },
                            {
                                "product": "prod_MqPwuMNDjnHJWJ",
                                "prices": ["price_1M6j70Cxk3VOyNJUHyaJ4IQ5"]
                            }
                        ],
                        "enabled": True,
                        "proration_behavior": "none"
                        }
                    }
                )
            # This is the URL to which the customer will be redirected after they are
            # done managing their billing with the portal.
            return_url = f"{FRONTEND_DOMAIN_URL}"

            portalSession = stripe.billing_portal.Session.create(
                customer=customer,
                return_url=return_url,
                configuration=portal_configuration
            )
            # print("portal: ", portalSession)
            data = {
                'stripe_url': portalSession.url
            }
            # print("DATA: ", data)
            return Response(data, status=200)
        except Exception as e:
            print("EXCEPTION: ", e)
            data = {
                'message': e
            }
            return Response(data, status=500)

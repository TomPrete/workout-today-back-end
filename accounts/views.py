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

stripe.api_key = 'sk_test_51LTVzmCxk3VOyNJUcsZ4S3O5C7y1p6tLcLw37L17reSYaZyIdSlUxMMKkboTgXo0sePUsYoJ5QdSEVvqiDAHJv6G00e0wdArHg'

development = True

FRONTEND_DOMAIN_URL = "https://workout-today.herokuapp.com/" if development == False else 'http://localhost:3000/'

print(FRONTEND_DOMAIN_URL)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomUserAuth(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        print(request.user)
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
    print("CUSTOMER: ", customer)
    update_user_with_stripe_id(customer)
    return customer

def update_user_with_stripe_id(stripe_customer):
    try:
        user_email = stripe_customer.email
        user = User.objects.get(email=user_email)
        user.stripe_id=stripe_customer.id
        user.save()
        return True
    except Exception as e:
       return False

def get_stripe_customer(user):
    customer = stripe.Customer.retrieve(user.stripe_id)
    return customer

def get_subscription_key(subscription_type):
    if subscription_type == 'monthly':
        price_id = 'price_1M6j70Cxk3VOyNJUHyaJ4IQ5'
    else:
        price_id = 'price_1M6jJPCxk3VOyNJUwyFqanWS'
    return price_id

class SubscriptionWebhook(APIView):
    # authentication_classes = [JWTAuthentication, TokenAuthentication]
    # permission_classes = []

    def post(self, request, format=None):
        print(request)
        data = {
            'message': 'subscription succeeded'
        }
        return Response(data, status=200)

class CheckoutSession(APIView):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = []

    def post(self, request, format=None):
        checkout_info = json.load(request)
        print('user: ', request.user)
        try:
            print(checkout_info)
            if request.user.stripe_id:
                stripe_customer = get_stripe_customer(request.user)
            else:
                stripe_customer = create_stripe_customer(request.user)
            print("STRIPE CUSTOMER: ", stripe_customer)
            price = stripe.Price.retrieve(
                get_subscription_key(checkout_info)
            )
            print("PRICE: ", price)
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': price.id,
                        'quantity': 1,
                    },
                ],
                subscription_data={
                    'trial_period_days': 7
                },
                automatic_tax={
                    'enabled': False
                },
                mode='subscription',
                customer=stripe_customer.id,
                success_url=f"{FRONTEND_DOMAIN_URL}checkout" +
                '?success=true&session_id={CHECKOUT_SESSION_ID}',
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
        user_info = json.load(request)
        try:
            stripe_id = request.user.stripe_id
            customer = get_stripe_customer(request.user)
            # This is the URL to which the customer will be redirected after they are
            # done managing their billing with the portal.
            return_url = f"{FRONTEND_DOMAIN_URL}"

            portalSession = stripe.billing_portal.Session.create(
                customer=customer,
                return_url=return_url,
            )
            print("portal: ", portalSession)
            return redirect(portalSession.url, code=303)
        except Exception as e:
            print("EXCEPTION: ", e)
            data = {
                'message': e
            }
            return Response(data, status=500)

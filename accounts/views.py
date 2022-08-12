from django.shortcuts import redirect
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
import stripe

stripe.api_key = 'sk_test_51LTVzmCxk3VOyNJUcsZ4S3O5C7y1p6tLcLw37L17reSYaZyIdSlUxMMKkboTgXo0sePUsYoJ5QdSEVvqiDAHJv6G00e0wdArHg'


FRONTEND_DOMAIN_URL = "http://localhost:3000/"

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
                'is_premium': request.user.is_premium
                })

        else:
            return Response({'message': 'user not logged in'})

class CheckoutSession(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        print("REQUEST: ", request.POST['lookup_key'])
        try:
            price = stripe.Price.retrieve(
                request.POST['lookup_key']
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
                    'enabled': True
                },
                mode='subscription',
                success_url="http://localhost:3000/checkout" +
                '?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url="http://localhost:3000/checkout" + '?canceled=true',
            )
            print("SESSION: ", checkout_session)
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            print(e)
            return "Server error", 500

@api_view(['POST'])
def checkout_session(request):
    print("REQUEST: ", request)
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

class CustomerPortalSession(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        checkout_session_id = request.POST['session_id']
        checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)

        # This is the URL to which the customer will be redirected after they are
        # done managing their billing with the portal.
        return_url = "http://localhost:3000/"

        portalSession = stripe.billing_portal.Session.create(
            customer=checkout_session.customer,
            return_url=return_url,
        )
        return redirect(portalSession.url, code=303)

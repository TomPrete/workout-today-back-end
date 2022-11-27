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


def get_customer_subscription(user):

    customer_subscription = stripe.Subscription.list(customer=user.stripe_id)
    print(customer_subscription)
    return customer_subscription

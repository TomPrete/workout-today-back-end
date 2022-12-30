from django.urls import path
from .views import MyTokenObtainPairView, CustomUserAuth, CheckoutSession, CustomerPortalSession, SubscriptionWebhook, change_password, reset_password, reset_password_confirm
reset_password_confirm
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/current_user/', CustomUserAuth.as_view(), name='current_user'),
    path('v1/change-password/', change_password, name='change_password'),
    path('v1/reset-password/', reset_password, name='reset_password'),
    path('v1/reset-password/<str:uuid>/', reset_password_confirm, name='reset_password_confirm'),
    path('create-checkout-session/', CheckoutSession.as_view(), name='checkout_session'),
    path('api/v1/create-portal-session/', CustomerPortalSession.as_view(), name='customer_portal'),
    path('api/v1/subscription-webhook/', SubscriptionWebhook.as_view(), name='subscription_webhook'),
]

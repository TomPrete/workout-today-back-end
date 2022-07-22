from django.urls import path
from .views import MyTokenObtainPairView, CustomUserAuth
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/current_user/', CustomUserAuth.as_view(), name='current_user'),
]

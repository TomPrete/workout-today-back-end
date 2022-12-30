"""workout_today URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('admin-site/', admin.site.urls),
    path('staff/', include('staff.urls')),
    path('api/', include('exercises.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/v1/accounts/', include('dj_rest_auth.urls')),
    path('api/v1/accounts/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('password_reset_complete')),
        name='password_reset_confirm'
    ),
    path('api/v1/accounts/reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
    path('api/v1/accounts/register/', include('dj_rest_auth.registration.urls')),
]

handler404 = "workout_today.views.page_not_found_view"

# a3b8bee7b193232f10dfe5e1963b6ad43cfad96f

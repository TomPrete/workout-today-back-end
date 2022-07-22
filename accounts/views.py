from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomUserAuth(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def  get(self, request, format=None):
        print(request.user)
        if request.user.is_authenticated:
            return Response({
                'username': request.user.username,
                'email': request.user.email,
                'is_premium': request.user.is_premium
                })

        else:
            return Response({'message': 'user not logged in'})


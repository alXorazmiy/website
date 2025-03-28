
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from .authentication import *


class LoginAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        

        if len(auth) == 2:
            token = auth[1].decode('utf-8')
            print(token)
            user_id = decode_token(token)
            user = User.objects.filter(id = user_id).values('email')
            return Response({
                'status': 200,
                "user": user
            })


    def post(self, request):
        print(request.data)
        email = request.data['email']
        password = request.data['password']

        user = User.objects.get(email = email)
        if not user:
            raise AuthenticationFailed('Not user')
        
        if not user.check_password("ab"+password):
            raise AuthenticationFailed("Uncorrect password")
        
        access_token = create_token(user.id)
        user = User.objects.filter(id = user.id).values('email')

        return Response({
            "token" : access_token,
            "user": user
        })



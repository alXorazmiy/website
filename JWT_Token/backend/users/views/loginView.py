

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from ..models import User
from ..service import createToken

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        print(email)
        print(password)

        user = User.objects.filter(email = email).first()

        if user is None:
            raise AuthenticationFailed("Foydalanuvchi topilmadi!")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Password xato!")
        
        token = createToken(user.id)
        response = Response()
        response.set_cookie(key="TOKEN", value = token, httponly = True)
        response.data = {
            "message": "success",
            "token" : token
        }
        
        return response



class LogoutAPIView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("TOKEN")
        response.data = {
            "message" : "success"
        }
        return response
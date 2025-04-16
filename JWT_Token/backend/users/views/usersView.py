from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from ..serializers import UserSerializers
from ..models import *
from ..service import *


class UserAPIView(APIView):
    def get(self, request):
        token = request.COOKIES.get("TOKEN")
        if not token:
            raise AuthenticationFailed("Ro'yxatdan o'tmagan!")
        
        user_id = decodeToken(token=token)
        user = User.objects.filter(id = user_id).first()
        serializer = UserSerializers(user)
        return Response(serializer.data)
    

class UsersListAPIView(APIView):
    def get(self, request):
        token = request.COOKIES.get("TOKEN")
        if not token:
            raise AuthenticationFailed("Ro'yxatdan o'tmagan!")
        user_id = decodeToken(token=token)
        user = User.objects.filter(id = user_id).first()
        if not user.is_staff:
            raise AuthenticationFailed("Xatolik!")
        users = User.objects.all()
        serializer = UserSerializers(users, many = True)    
        return Response(serializer.data)




class UserDetailAPIView(APIView):


    def get(self, request, pk):
        try:
            user = User.objects.get(pk = pk)
        except User.DoesNotExist:
            return Response({"detail": "Foydalanuvchi topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializers(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        
        except User.DoesNotExist:
            return Response({"detail": "Foydalanuvchi topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializers(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk = pk)
        except User.DoesNotExist:
            return Response({'detail': "Foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import User
from ..serializers import UserSerializers
from ..service import createToken


class RegisterAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if User.objects.filter(email=email).exists():
            return Response({"error": "Bu email allaqachon ro'yxatdan o'tgan"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        serializer = UserSerializers(data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            token = createToken(user.id)
            response = Response({
                "message": "User created successfully",
                "token": token,
            }, status=status.HTTP_201_CREATED)
        
            response.set_cookie(key="TOKEN", value=token, httponly=True)
            return response
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
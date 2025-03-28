from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header


from user.models import CustomUser
from api.models import *
from api.authentication import *
from api.serializer import UserSerializer

class LoginAPIView(APIView):

    def get(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            users = CustomUser.objects.get(id = user_id)
            serializer = UserSerializer(users)
            return Response(serializer.data)

    def post(self, request):
        username = request.data['username']
        password =request.data['password']
        user = CustomUser.objects.filter(username = username).first()
        
        if not user:
            raise AuthenticationFailed("Bunday foydalanuvchi yo'q")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Parol noto'g'ri")
        
        access_token = create_token(user.id)
        
        return Response({
            "token": access_token,
            'user': UserSerializer(user).data
        })

   
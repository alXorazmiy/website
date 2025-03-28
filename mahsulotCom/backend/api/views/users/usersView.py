from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from api.authentication import decode_token
from user.models import CustomUser
from api.serializer import UserSerializer


class UsersAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            users = CustomUser.objects.all()
            serializer = UserSerializer(users, many = True)
            return Response(serializer.data)
        
    def post(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)

            user = CustomUser.objects.create(
                username = request.data['username'],
                role = request.data['role'],
                is_active = True if request.data['active'] == 'true' else False
            )
            user.set_password(request.data['password'])
            user.save()

            users = CustomUser.objects.all()
            serializer = UserSerializer(users, many = True)
            return Response(serializer.data)
        

class UserDetailAPIView(APIView):
    def put(self, request, pk):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)

            user = CustomUser.objects.get(id = pk)
            user.username = request.data['username']
            user.role = request.data['role']
            user.is_active = True if request.data['active'] == 'true' else False

            if request.data['password'] != '********':
                user.set_password(request.data['password'])
            user.save()

            users = CustomUser.objects.all()
            serializer = UserSerializer(users, many = True)
            return Response(serializer.data)
        

    def delete(self, request, pk):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)

            user = CustomUser.objects.get(id = pk).delete()

            users = CustomUser.objects.all()
            serializer = UserSerializer(users, many = True)
            return Response(serializer.data)


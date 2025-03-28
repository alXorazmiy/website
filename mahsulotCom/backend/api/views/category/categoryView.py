from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from api.authentication import decode_token
from api.models import Category
from api.serializer import ShopSerializer


class CategoryAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            categories = Category.objects.all().values()
            return Response({
                'categories' : categories
            })
        
    def post(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)

            category = Category.objects.create(
                title = request.data['title'],
                description = request.data['description'],
                # image = request.data['image']
            )
            category.save()

            categories = Category.objects.all().values()
            return Response({
                'categories' : categories
            })
    
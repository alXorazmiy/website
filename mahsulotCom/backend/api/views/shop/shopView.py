from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from api.authentication import decode_token
from api.models import Shop
from api.serializer import ShopSerializer


class ShopAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            shops = Shop.objects.all().values()
            return Response({
                'shops' : shops
            })
        
    def post(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)

            shop = Shop.objects.create(
                title = request.data['title'],
                description = request.data['description'],
                image = request.data['image']
            )
            shop.save()

            shops = Shop.objects.all().values()
            return Response({
                'shops' : shops
            })
    

class ShopDetailAPIView(APIView):
    def get(self, request, pk):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            shops = Shop.objects.get(id = pk)
            serializer = ShopSerializer(shops)
            return Response(serializer.data)
        

    def put(self, request, pk):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            shops = Shop.objects.get(id = pk)

            shops.title = request.data['title']
            shops.description = request.data['description']
            shops.image = request.data['image']
            shops.save()

            serializer = ShopSerializer(shops)
            return Response(serializer.data)
        
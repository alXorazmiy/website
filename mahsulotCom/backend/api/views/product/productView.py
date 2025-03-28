from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from api.authentication import decode_token
from api.models import Product, Shop, Category
from api.serializer import ProductSerializer


class ProductAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            shops = Product.objects.all().values()
            return Response({
                'shops' : shops
            })
    

class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            shops = Product.objects.all().values()
            return Response({
                'shops' : shops
            })
        
    def put(self, request, pk):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            shop = Shop.objects.get(id = int(request.data['id']))
            category = Category.objects.get(title = request.data['category'])
      

            product = Product.objects.get(id = pk)

            product.title = request.data['title']
            product.description = request.data['description']
            product.price = request.data['price']
            product.amount = request.data['amount']
            product.active = True if request.data['active'] == 'true' else False
            product.image = request.data['images']
            product.shop = shop
            product.category = category
            product.save()


            products = Product.objects.filter(shop = shop)
            serializer = ProductSerializer(products, many = True)
            return Response(serializer.data)
        

    def delete(self, request, pk):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            product = Product.objects.get(id = pk)

            shop = Shop.objects.get(id = product.shop_id)

            product.delete()


            products = Product.objects.filter(shop = shop)
            serializer = ProductSerializer(products, many = True)
            return Response(serializer.data)



class ShopProductsAPIView(APIView):
    def get(self, request, pk):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            shop = Shop.objects.get(id = pk)
            products = Product.objects.filter(shop = shop)
            serializer = ProductSerializer(products, many = True)
            return Response(serializer.data)
        

    def post(self, request, pk):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            shop = Shop.objects.get(id = pk)
            category = Category.objects.get(id = request.data['category'])
            product = Product.objects.create(
                title = request.data['title'],
                description = request.data['description'],
                price = request.data['price'],
                amount = request.data['amount'],
                active = True if request.data['active'] == 'true' else False,
                image = request.data['images'],
                shop = shop,
                category = category
            )
            product.save()
            products = Product.objects.filter(shop = shop)
            serializer = ProductSerializer(products, many = True)
            return Response(serializer.data)
        
    def put(self, request, pk):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            shop = Shop.objects.get(id = pk)
            products = Product.objects.filter(shop = shop)

            print(request.data)
            if request.data['active'] != 'all':
                products = products.filter(active = True if request.data['active'] == 'true' else False)

            if request.data['price_1'] != 'null' and request.data['price_2'] != 'null' and request.data['price_1'] != '' and request.data['price_2'] != '':
                products = products.filter(price__gte = request.data['price_1'], price__lte = request.data['price_2'])
                



            
            serializer = ProductSerializer(products, many = True)
            return Response(serializer.data)
        

    
from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from api.authentication import decode_token
from api.models import Image
from api.serializer import ImageSerializer


class ImageAPIView(APIView):
    def post(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) ==  2:
            print(request.data['image'])
            token = auth[1].decode('utf-8')
            user_id = decode_token(token)
            image = Image.objects.create(
                image = request.data['image']
            )
            image.save()
            serializer = ImageSerializer(image, context = {'request' : request})

            return Response(serializer.data)
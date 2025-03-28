from rest_framework.views import APIView
from rest_framework.response import Response 
from api.models import Image
from api.serializers import ImageSerializer



class ImageAPIView(APIView):
    def post(self, request):
        image = request.data['image']
        image = Image.objects.create(
            image = image
        )
        image.save()
        serializer = ImageSerializer(image, context = {'request' : request})
        return Response(serializer.data)

    
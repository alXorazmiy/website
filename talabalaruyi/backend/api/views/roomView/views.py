from rest_framework.views import APIView
from rest_framework.response import Response 
from api.models import Floor, Room
from api.serializers import RoomSerializer



class RoomsAPIView(APIView):
    def get(self, request, pk):
        floor = Floor.objects.get(number = pk)
        rooms = Room.objects.filter(floor = floor)
        serializer = RoomSerializer(rooms, many = True)
        return Response(serializer.data)
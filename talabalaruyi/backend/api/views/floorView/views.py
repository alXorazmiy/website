from rest_framework.views import APIView
from rest_framework.response import Response 
from api.models import Floor, Room
from api.serializers import FloorSerializer



class FloorsAPIView(APIView):
    def get(self, request):
        floor = Floor.objects.all()
        serializer = FloorSerializer(floor, many = True)
        return Response(serializer.data)
        


    def post(self, request):
        floor = Floor.objects.all()
        if not floor:
            number = 1
        else:
            number = floor.last().number + 1
        new_floor = Floor.objects.create(
            number = number,
            empty_place = 48,
            busy_place = 0
        )
        new_floor.save()

        for i in range(12):
            room = Room.objects.create(
                number = i + 1,
                floor = new_floor,
                place = 4,
                beds = [  False,False, False, False ]
            )
            room.save()


        floor = Floor.objects.all()
        serializer = FloorSerializer(floor, many = True)
        return Response(serializer.data)
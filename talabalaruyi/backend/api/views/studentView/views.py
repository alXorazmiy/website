
from rest_framework.views import APIView
from rest_framework.response import Response 
from api.models import *
from api.serializers import StudentSerializer, AllStudentSerializer



class StudentAPIView(APIView):
    def get(self, request):
        id = request.GET.get('student')
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def post(self, request):
        floor = Floor.objects.get(number = request.data['floor'])
        room = Room.objects.get(floor = floor, number = request.data['room'])
        faculty = Faculty.objects.get(id = request.data['faculty'])
        beds = room.beds 

        student = Student.objects.create(
            first_name = request.data['first_name'],
            last_name = request.data['last_name'],
            course = request.data['course'],
            faculty = faculty,
            image=  request.data['image'],
            in_time = request.data['date'],
            floor= request.data['floor'],
            room = request.data['room'],
            bed = request.data['bed']
        )
        student.save()


        beds[request.data['bed'] - 1] = student.id
        floor.empty_place = floor.empty_place - 1 
        floor.busy_place = floor.busy_place + 1 
        floor.save()

        room.beds = beds 
        room.save()
        return Response(status=200)
    
    def delete(self, request):
        id = request.GET.get('student')
        student = Student.objects.get(id = id)
        floor = Floor.objects.get(number = student.floor)

        room = Room.objects.get(floor = floor, number = student.room)
        beds = room.beds
        beds[student.bed - 1] = False
        room.beds = beds 
        room.save()

        floor.empty_place = floor.empty_place + 1 
        floor.busy_place = floor.busy_place - 1 
        floor.save()

        return Response(status=200)

    

class AllStudentsAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = AllStudentSerializer(students, many = True)
        return Response(serializer.data)
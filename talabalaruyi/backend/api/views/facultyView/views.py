from rest_framework.views import APIView
from rest_framework.response import Response 
from api.models import Faculty
from api.serializers import FacultySerializer



class FacultyAPIView(APIView):
    def get(self, request):
        faculty = Faculty.objects.all()
        serializer = FacultySerializer(faculty, many = True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data['name']
        faculty = Faculty.objects.create(
            name = name
        )
        faculty.save()
        faculty = Faculty.objects.all()
        serializer = FacultySerializer(faculty, many = True)
        return Response(serializer.data)

    
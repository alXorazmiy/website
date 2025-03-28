from rest_framework import serializers
from .models import *


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor 
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    floor = FloorSerializer()
    class Meta:
        model = Room
        fields = "__all__"


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty 
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image 
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = "__all__"

class AllStudentSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer()
    class Meta:
        model = Student 
        fields = "__all__"

class PaymentsSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = Payments 
        fields = "__all__"

from django.urls import path 
from api.views.floorView.views import FloorsAPIView
from api.views.roomView.views import RoomsAPIView
from api.views.facultyView.views import FacultyAPIView
from api.views.imageView.views import ImageAPIView
from api.views.studentView.views import StudentAPIView, AllStudentsAPIView
from api.views.paymentView.views import PaymentAPIView

urlpatterns =[
    path('floor/', FloorsAPIView.as_view()),
    path('rooms/<int:pk>/', RoomsAPIView.as_view()),
    path("faculty/", FacultyAPIView.as_view()),
    path('image/', ImageAPIView.as_view()),
    path('student/', StudentAPIView.as_view()),
    path('allstudents/', AllStudentsAPIView.as_view()),
    path('payments/', PaymentAPIView.as_view()),
]
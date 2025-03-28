
from rest_framework.views import APIView
from rest_framework.response import Response 
from api.models import *
from api.serializers import PaymentsSerializer



class PaymentAPIView(APIView):
    def get(self, request):
        print(request.GET.get('student'))
        if request.GET.get('student') == None:
            payments = Payments.objects.all()
            
        else:
            payments = Payments.objects.filter(student__id = request.GET.get('student'))
        serializer = PaymentsSerializer(payments, many = True)
        return Response(serializer.data)


    def post(self, request):
        student = Student.objects.get(id = request.data['student'])
        amount = request.data['amount']
        payment = Payments.objects.create(
            student = student,
            amount = amount
        )
        payment.save()
        payments = Payments.objects.all()
        serializer = PaymentsSerializer(payments, many = True)
        return Response(serializer.data)

    

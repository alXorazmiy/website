


from rest_framework.views import APIView 
from rest_framework.response import Response
from .pusher import *


class MessageAPIView(APIView):
    def post(self, request):
        pusher_client.trigger('chat', 'message', {
            'id': request.data['id'],
            'username': request.data['username'],
            'message' : request.data['message'],
            'date': request.data['date']
        })

        return Response([])
        
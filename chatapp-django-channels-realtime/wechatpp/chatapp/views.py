from django.shortcuts import render
from .models import Room, Message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import RoomSerializer
from django.http import Http404
def rooms(request):
    rooms=Room.objects.all()
    return render(request, "rooms.html",{"rooms":rooms})

def room(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    
    return render(request, "room.html",{"room_name":room_name,"slug":slug,'messages':messages})
class RoomList(APIView):
    """
    List all rooms or create a new room.
    """
    def get(self, request, format=None):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomDetail(APIView):
    """
    Retrieve, update or delete a room instance.
    """
    def get_object(self, slug):
        try:
            return Room.objects.get(slug=slug)
        except Room.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        room = self.get_object(slug)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        room = self.get_object(slug)
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        room = self.get_object(slug)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

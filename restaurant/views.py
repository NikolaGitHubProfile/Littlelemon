from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics , status

from . import models
from . import serializers

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

class BookingView(APIView):

    def get(self, request):
        print(request.GET)
        items = models.Booking.objects.all()
        serializer = serializers.BookingSerializer(items, many=True)

        return Response(serializer.data) #Returns JSON
    
    def post(self, request):
        serializer = serializers.BookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data' : serializer.data}, status=status.HTTP_201_CREATED)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
        
class MenuItemView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

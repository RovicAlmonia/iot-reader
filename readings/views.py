from rest_framework import viewsets
from .models import Building, PowerReading
from .serializers import BuildingSerializer, PowerReadingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class PowerReadingViewSet(viewsets.ModelViewSet):
    queryset = PowerReading.objects.all().order_by('-timestamp')
    serializer_class = PowerReadingSerializer

    @action(detail=False, methods=['get'])
    def average_power(self, request):
        data = PowerReading.objects.values('building__name').annotate(avg_power=Avg('power_kw'))
        return Response(data)

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RegisterUser(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
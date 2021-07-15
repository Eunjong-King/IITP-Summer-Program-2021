from rest_framework.serializers import ModelSerializer
from .models import Data, Device

class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ['device', 'value', 'time']
        
class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ['device1', 'device2', 'device3', 'device4']
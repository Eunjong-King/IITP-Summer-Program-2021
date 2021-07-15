from django.contrib import admin
from .models import Data, Device

# Register your models here.
class showDataDetail(admin.ModelAdmin):
    list_display=('device','value','time',)

class showDeviceDetail(admin.ModelAdmin):
    list_display=('device1','device2','device3','device4')
    

admin.site.register(Data, showDataDetail)
admin.site.register(Device, showDeviceDetail)
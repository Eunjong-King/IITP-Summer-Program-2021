from django.contrib import admin
from .models import Data

# Register your models here.
class showdetail(admin.ModelAdmin):
    list_display=('device','value','time',)

admin.site.register(Data, showdetail)
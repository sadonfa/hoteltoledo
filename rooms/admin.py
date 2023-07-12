from django.contrib import admin
from .models import Rooms

# Register your models here.

class RoomsAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    
admin.site.register(Rooms, RoomsAdmin)
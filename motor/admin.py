from django.contrib import admin
from .models import Disponibilidad, Rooms, Plan

# Register your models here.

class RoomsAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    
admin.site.register(Rooms, RoomsAdmin)

class PlanAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    
admin.site.register(Plan, PlanAdmin)

class MotorAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    
admin.site.register(Disponibilidad, MotorAdmin)
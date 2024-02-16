from django.contrib import admin
from .models import Slider,About,Services,Doctors
@admin.register(Slider)

class SliderAdmin(admin.ModelAdmin):
    list_display = ('text',)
 

@admin.register(About)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('text',)
 
@admin.register(Services)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Doctors)

class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('name',)

    
    

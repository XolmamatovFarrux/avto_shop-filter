from django.contrib import admin
from .models import Car, Car_s


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand','created_at','updated_at')
    list_filter = ('created_at','updated_at')
    search_fields = ('brand','year')
    ordering = ('-id',)


class Car_sAdmin(admin.ModelAdmin):
    list_display = ('title','brand','color','year','price','image'  ,'created_at','updated_at')
    list_filter = ('title','brand','color','year','price','image','context')
    search_fields = ('brand','title')
    ordering = ('-id',)


admin.site.register(Car,CarAdmin)
admin.site.register(Car_s,Car_sAdmin)

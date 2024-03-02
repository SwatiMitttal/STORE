from django.contrib import admin
from .models import Customer
# Register your models here.
class Cadmin(admin.ModelAdmin):
    prepopulated_fields={}
    
admin.site.register(Customer)
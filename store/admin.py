from django.contrib import admin
from  .models import Product,Category,Design
# Register your models here.

class Padmin(admin.ModelAdmin):
    list_display=['pname','price','desc','images']
    prepopulated_fields={'slug':'pname'}
    
class Cadmin(admin.ModelAdmin):
    list_display=['cname']
    prepopulated_fields={'slug':'cname'}

admin.site.register(Design)
admin.site.register(Product)
admin.site.register(Category)

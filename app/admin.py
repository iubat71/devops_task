from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Package)
# admin.site.register(Card)
# admin.site.register(Status)
admin.site.register(Product_refill)
admin.site.register(Package_refill)



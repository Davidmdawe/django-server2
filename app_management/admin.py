from django.contrib import admin

# Register your models here.
from .models import Inside,Outside,Menu,Mccafe as McCafe,Drivethru as Drivethru,Delivery as Delivery, Shops
admin.site.register(Shops)
admin.site.register(Inside)
admin.site.register(Outside)
admin.site.register(Menu)
admin.site.register(McCafe)
admin.site.register(Drivethru)
admin.site.register(Delivery)
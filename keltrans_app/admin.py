from django.contrib import admin
from django.urls import path, include
from keltrans_app.models import User, Carrier

from django.contrib.auth.admin import UserAdmin

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

class CarrierAdmin(admin.ModelAdmin):
    pass
admin.site.register(Carrier, CarrierAdmin)

urlpatters = [
    path('admin/',admin.site.urls),
    path('', include("keltrans_app.urls"))
]

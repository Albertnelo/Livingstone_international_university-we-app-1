from django.contrib import admin
from .models import New_User
# Register your models here.


class New_userAdmin(admin.ModelAdmin):
    list_display=('Name','Password')
admin.site.register(New_User,New_userAdmin)
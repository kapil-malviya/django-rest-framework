from django.contrib import admin
from .models import Manager  



class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'city')  


admin.site.register(Manager, ManagerAdmin)
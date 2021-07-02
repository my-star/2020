from django.contrib import admin
from .models import Department,MatUser,Computer
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    pass
class MatUserAdmin(admin.ModelAdmin):
    pass
class ComputerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Department,DepartmentAdmin),
admin.site.register(MatUser,MatUserAdmin),
admin.site.register(Computer,ComputerAdmin),

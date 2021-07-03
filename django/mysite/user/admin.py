from django.contrib import admin
from .models import User,Log,Record,Depart
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','emp_num']

class LogAdmin(admin.ModelAdmin):
    list_display = ['time','user','record','action']

class RecordAdmin(admin.ModelAdmin):
    list_display = ['record_text','username','depart','record_time']

class DepartAdmin(admin.ModelAdmin):
    pass
admin.site.register(Log ,LogAdmin),
admin.site.register(User,UserAdmin)
admin.site.register(Record,RecordAdmin)
admin.site.register(Depart,DepartAdmin)

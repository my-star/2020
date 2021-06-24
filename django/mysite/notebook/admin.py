from django.contrib import admin
from notebook.models import User,Depart,Record
# Register your models here.

class UserAdmin (admin.ModelAdmin):
    pass
class DepartAdmin(admin.ModelAdmin):
    pass
class RecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Depart, DepartAdmin)
admin.site.register(Record, RecordAdmin)

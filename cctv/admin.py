from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Manager

# Register your models here.
class ManagerInline(admin.StackedInline):
    model = Manager
    can_delete = False
    verbose_name_plural = 'Manager'

class UserAdmin(UserAdmin):
    inlines = (ManagerInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
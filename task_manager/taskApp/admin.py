from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taskApp.models import Profile,Task
from django.contrib.auth.models import User
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class Admin_Task(admin.ModelAdmin):
    list_display = ['task_name', 'description','status', 'worker','get_assign_to','created_by','created_on']


admin.site.register(Task,Admin_Task)
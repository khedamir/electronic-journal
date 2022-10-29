from django.contrib import admin

# Register your models here.

from .models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class StudentInLine(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'


class UserAdmin(BaseUserAdmin):
    inlines = (StudentInLine,)



admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(Lesson)
admin.site.register(StudentGroup)
admin.site.register(Discipline)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Mark)

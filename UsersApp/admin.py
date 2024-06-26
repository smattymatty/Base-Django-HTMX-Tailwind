from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)

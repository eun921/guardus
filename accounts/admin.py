from django.contrib import admin
from .models import Profile
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile)
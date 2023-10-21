from django.contrib import admin
from enroll.models import user

# Register your models here.
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')
from django.contrib import admin

# Register your models here.
from .models import Job


class JobAdmin(admin.ModelAdmin):
    class Meta:
        model = Job
    
admin.site.register(Job,JobAdmin)
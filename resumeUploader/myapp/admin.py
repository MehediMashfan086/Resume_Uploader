from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'zipcode',
                    'state', 'mobile', 'job_city', 'profile_image', 'my_file']

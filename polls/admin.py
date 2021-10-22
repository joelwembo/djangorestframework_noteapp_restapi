from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question

# add tge aoo to admin
admin.site.register(Question)
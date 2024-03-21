from django.contrib import admin

from .models import Project,Posts

# Register your models here.
admin.site.register(Project),
admin.site.register(Posts)
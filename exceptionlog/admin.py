from django.contrib import admin
from .models import exceptionlogs

# Register your models here.

@admin.register(exceptionlogs)
class TaskAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    list_display = ('filename', 'lineno', 'code', 'type', 'time')


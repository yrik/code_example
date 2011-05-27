from django.contrib import admin

from core.models import Person, Log


class LogAdmin(admin.ModelAdmin):
        list_display = ('date', 'priority', 'content')
        list_filter = ('priority',)
        ordering = ['date', '-priority']

admin.site.register(Person)
admin.site.register(Log, LogAdmin)

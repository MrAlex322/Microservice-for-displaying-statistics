from django.contrib import admin

from .models import Statistics


# Register your models here.

class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('date', 'views', 'clicks', 'cost')
    ordering = ('-date','-views', '-clicks')


admin.site.register(Statistics, StatisticsAdmin)

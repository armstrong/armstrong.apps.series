from django.contrib import admin
from django.contrib.contenttypes import generic


from . import models


class SeriesNodeInline(generic.GenericTabularInline):
    model = models.SeriesNode


class SeriesAdmin(admin.ModelAdmin):
    model = models.Series

    inlines = [
        'SeriesNodeInline',
    ]


admin.site.register(models.Series, SeriesAdmin)

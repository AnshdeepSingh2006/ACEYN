from django.contrib import admin
from .models import Games1, Games2, Games3


class Games1Admin(admin.ModelAdmin):
    list_display = ('name', 'rate')


class Games2Admin(admin.ModelAdmin):
    list_display = ('name', 'rate')


class Games3Admin(admin.ModelAdmin):
    list_display = ('name', 'rate')


admin.site.register(Games1, Games1Admin)
admin.site.register(Games2, Games2Admin)
admin.site.register(Games3, Games3Admin)

from django.contrib import admin
from .models import NewGame


class NewGameAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate')


admin.site.register(NewGame, NewGameAdmin)

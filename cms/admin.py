from django.contrib import admin
from cms.models import Todo
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'duty', 'limit')
    list_display_links = ('id', 'duty', 'limit')


admin.site.register(Todo, TodoAdmin)

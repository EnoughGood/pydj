from django.contrib import admin
from sign.models import Event, Guest

"""
    映射models 中的数据到Django 带自的admin 后台
"""


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time', 'id']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)

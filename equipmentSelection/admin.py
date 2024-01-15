from django.contrib import admin
from .models import Equipment, FSMotors, FCMotors


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rendering_order')


class FSMotorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'rendering_order')


class FCMotorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'rendering_order')


admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(FSMotors, FSMotorsAdmin)
admin.site.register(FCMotors, FCMotorsAdmin)

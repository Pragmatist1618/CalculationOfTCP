from django.contrib import admin
from .models import Equipment, FSMotors, FCMotors, Supplier, EquipmentType, PLC, PLCExpansionModule, HMI


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rendering_order')


class FSMotorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'rendering_order')


class FCMotorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'rendering_order')


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'discount', 'markup')


class EquipmentTypeAdmin(admin.ModelAdmin):
    # list_display = ('name', )
    pass


class PLCAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'supplier')

    model = PLC

    # def get_form(self, request, obj=None, **kwargs):
    #     # Получаем форму от базового класса
    #     form = super().get_form(request, obj, **kwargs)
    #
    #     # Определите здесь идентификатор производителя Siemens
    #     siemens_manufacturer_id = Supplier.objects.get(supplier_name='Siemens').id
    #
    #     # Скрыть поле model, если производитель не Siemens
    #     form.base_fields['model'].widget.attrs['style'] = 'display:none;'
    #     form.base_fields['model'].required = False
    #
    #     # Добавить JavaScript-класс для скрытия/отображения поля model
    #     form.base_fields['supplier'].widget.attrs['class'] = 'supplier-dropdown'
    #     form.base_fields['model'].widget.attrs['class'] = 'model-dropdown'
    #
    #     # Добавить атрибут data-siemens-id с идентификатором производителя Siemens
    #     form.base_fields['supplier'].widget.attrs['data-siemens-id'] = siemens_manufacturer_id
    #
    #     return form

    # Динамическое скрытие поля model, если ПЛК не Siemens
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.4.min.js', 'equipmentSelection/js/admin.js', )


class PLCExpansionModuleAdmin(admin.ModelAdmin):
    # list_display = ('name', )
    pass


class HMIAdmin(admin.ModelAdmin):
    # list_display = ('name', )
    pass


admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(FSMotors, FSMotorsAdmin)
admin.site.register(FCMotors, FCMotorsAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(EquipmentType, EquipmentTypeAdmin)
admin.site.register(PLC, PLCAdmin)
admin.site.register(PLCExpansionModule, PLCExpansionModuleAdmin)
admin.site.register(HMI, HMIAdmin)

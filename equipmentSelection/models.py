# equipmentSelection/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class Equipment(models.Model):
    rendering_order = models.IntegerField(
        blank=True,
        null=True,
        unique=True,
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    analog_input_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )
    analog_input_RTD_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )
    analog_output_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )
    discrete_input_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )
    discrete_output_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )
    pneumatic_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Equipment_list"
        ordering = ['rendering_order']


class FSMotors(models.Model):
    rendering_order = models.IntegerField(
        blank=True,
        null=True,
        unique=True,
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    analog_input_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )
    analog_input_RTD_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )
    analog_output_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )
    discrete_input_count = models.IntegerField(
        blank=True,
        null=True,
        default=3,
    )
    discrete_output_count = models.IntegerField(
        blank=True,
        null=True,
        default=1,
    )
    pneumatic_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "FSMotors_list"
        ordering = ['rendering_order']


class FCMotors(models.Model):
    rendering_order = models.IntegerField(
        blank=True,
        null=True,
        unique=True,
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    analog_input_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )
    analog_input_RTD_count = models.IntegerField(
        blank=True,
        null=True,
        default=1,
    )
    analog_output_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )
    discrete_input_count = models.IntegerField(
        blank=True,
        null=True,
        default=3,
    )
    discrete_output_count = models.IntegerField(
        blank=True,
        null=True,
        default=1,
    )
    pneumatic_count = models.IntegerField(
        blank=True,
        null=True,
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "FCMotors_list"
        ordering = ['rendering_order']


def validate_communication_type(value):
    valid_communication_types = ['profibus', 'profinet']
    if value not in valid_communication_types:
        raise ValidationError("Invalid communication type. Choose from: profibus, profinet.")


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=255)
    discount = models.FloatField(validators=[MinValueValidator(0.0)], default=0, verbose_name ='Discount, %')
    markup = models.FloatField(validators=[MinValueValidator(0.0)], default=1, verbose_name ='Sales ratio')

    def __str__(self):
        return self.supplier_name


class EquipmentType(models.Model):
    type_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.type_name


# class Automation(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     code = models.CharField(max_length=255)
#     cost = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
#     equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)


class PLC(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    model = models.IntegerField(choices=[(1, 'Simatic S7-1200'), (2, 'Simatic S7-1500'), (3, 'Simatic S7-300'), (3, 'Simatic S7-400')], blank=True, null=True)
    code = models.CharField(max_length=255, default='')
    cost = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True, verbose_name ='Cost, €')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    communication_profinet = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    communication_profibus = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    max_expansion_modules = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    power_supply_type = models.IntegerField(choices=[(24, '24V'), (220, '220V'), (380, '380V')], default=24)
    power_consumption = models.FloatField(validators=[MinValueValidator(0.0)], default=0)
    power_dissipation = models.FloatField(validators=[MinValueValidator(0.0)], default=0)
    digital_inputs = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    digital_outputs = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    analog_inputs = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    analog_inputs_rtd = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    analog_outputs = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.name


class HMI(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, default='')
    cost = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    screen_diagonal = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    communication_type = models.IntegerField(choices=[(1, 'profinet'), (2, 'profibus')])
    power_supply_type = models.IntegerField(choices=[(24, '24V'), (220, '220V'), (380, '380V')], default=24)
    power_consumption = models.FloatField(validators=[MinValueValidator(0.0)], default=0)
    power_dissipation = models.FloatField(validators=[MinValueValidator(0.0)], default=0)

    def __str__(self):
        return self.name


class PLCExpansionModule(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, default='')
    cost = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    power_supply_type = models.IntegerField(choices=[(24, '24V'), (220, '220V'), (380, '380V')], default=24)
    power_consumption = models.FloatField(validators=[MinValueValidator(0.0)], default=0)
    digital_inputs = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    digital_outputs = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    analog_inputs = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    analog_inputs_rtd = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    analog_outputs = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.name

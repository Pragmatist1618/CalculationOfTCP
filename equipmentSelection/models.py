# equipmentSelection/models.py
from django.db import models


class Equipment(models.Model):
    rendering_order = models.IntegerField(
        max_length=255,
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
        max_length=255,
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
        max_length=255,
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

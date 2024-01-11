# equipmentSelection/models.py
from django.db import models


class Equipment(models.Model):
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

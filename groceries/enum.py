from django.db import models
from django.utils.translation import gettext_lazy as _

class MeasuringUnits(models.TextChoices):
    LITRE = 'LT', _("lt")
    MILLILITRE = 'ML', _("ml")
    KILOGRAM = 'KG', _("kg")
    GRAM = 'G', _("g")
    NUMBER = 'NOS', _("nos")
    PACK = 'PK', _("pack")
    ROLL = 'RL', _("roll")
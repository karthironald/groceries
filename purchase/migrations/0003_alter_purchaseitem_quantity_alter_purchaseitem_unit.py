# Generated by Django 4.1.3 on 2022-12-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchase", "0002_alter_purchaseitem_unit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchaseitem",
            name="quantity",
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name="purchaseitem",
            name="unit",
            field=models.CharField(
                choices=[
                    ("LT", "Litre"),
                    ("ML", "Millilitre"),
                    ("KG", "Kilogram"),
                    ("G", "Gram"),
                    ("NOS", "Number"),
                    ("PK", "Pack"),
                    ("RL", "Roll"),
                ],
                default="nos",
                max_length=100,
            ),
        ),
    ]

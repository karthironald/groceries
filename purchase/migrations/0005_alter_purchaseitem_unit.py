# Generated by Django 4.1.3 on 2022-12-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchase", "0004_alter_purchaseitem_unit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchaseitem",
            name="unit",
            field=models.CharField(
                choices=[
                    ("LT", "lt"),
                    ("ML", "ml"),
                    ("KG", "kg"),
                    ("G", "g"),
                    ("NOS", "nos"),
                    ("PK", "pack"),
                    ("RL", "roll"),
                ],
                default="nos",
                max_length=100,
            ),
        ),
    ]

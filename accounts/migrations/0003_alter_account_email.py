# Generated by Django 4.2.4 on 2023-09-06 01:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="email",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-31 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nam", models.CharField(default="", max_length=30)),
                ("add1", models.CharField(default="", max_length=50)),
                ("mail", models.EmailField(default="example@gmal.com", max_length=50)),
                ("phone", models.TextField(default="10 digit number", max_length=12)),
                ("addedat", models.DateTimeField(default="")),
                ("add2", models.CharField(default="", max_length=100)),
                ("city", models.CharField(default="", max_length=50)),
                ("state", models.CharField(default="", max_length=50)),
            ],
        ),
    ]
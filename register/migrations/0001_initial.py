# Generated by Django 5.0.1 on 2024-03-04 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("fname", models.CharField(max_length=50)),
                ("lname", models.CharField(max_length=50)),
                ("uname", models.CharField(max_length=50, unique=True)),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("mobile", models.CharField(max_length=50)),
                ("dadd", models.DateTimeField(auto_now_add=True)),
                ("llogin", models.DateTimeField(auto_now_add=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_sadmin", models.BooleanField(default=False)),
            ],
        ),
    ]
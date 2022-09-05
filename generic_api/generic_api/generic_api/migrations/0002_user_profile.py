# Generated by Django 4.1 on 2022-09-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("generic_api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("about_me", models.CharField(max_length=2048)),
            ],
        ),
    ]
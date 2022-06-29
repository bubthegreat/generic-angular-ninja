# Generated by Django 4.0.4 on 2022-05-13 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("skill_matrix_api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Competency",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="FunctionalArea",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="KeyArea",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Level",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="LevelDescription",
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
                ("title", models.CharField(max_length=100)),
                (
                    "competency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="skill_matrix_api.competency",
                    ),
                ),
                (
                    "functional_area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="skill_matrix_api.functionalarea",
                    ),
                ),
                (
                    "key_area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="skill_matrix_api.keyarea",
                    ),
                ),
                (
                    "level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="skill_matrix_api.level",
                    ),
                ),
            ],
        ),
    ]

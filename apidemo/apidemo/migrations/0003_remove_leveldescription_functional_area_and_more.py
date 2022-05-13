# Generated by Django 4.0.4 on 2022-05-13 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apidemo', '0002_competency_functionalarea_keyarea_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leveldescription',
            name='functional_area',
        ),
        migrations.RemoveField(
            model_name='leveldescription',
            name='key_area',
        ),
        migrations.AddField(
            model_name='competency',
            name='functional_area',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='apidemo.functionalarea'),
        ),
        migrations.AddField(
            model_name='functionalarea',
            name='key_area',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='apidemo.keyarea'),
        ),
    ]

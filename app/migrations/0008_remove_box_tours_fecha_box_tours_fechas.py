# Generated by Django 4.2 on 2023-04-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_box_tours_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box_tours',
            name='fecha',
        ),
        migrations.AddField(
            model_name='box_tours',
            name='fechas',
            field=models.CharField(default=False, max_length=10),
        ),
    ]

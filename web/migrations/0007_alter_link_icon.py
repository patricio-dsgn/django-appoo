# Generated by Django 4.0.4 on 2022-05-04 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_tip_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='icon',
            field=models.CharField(choices=[('web', 'fa-solid fa-globe'), ('salud', 'fa-solid fa-house-medical'), ('otros', 'fa-solid fa-link')], max_length=100),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-12 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_passajir_passport_alter_static_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='static',
            name='data_prileta',
            field=models.DateTimeField(verbose_name='Прилёт (дата и время)'),
        ),
    ]
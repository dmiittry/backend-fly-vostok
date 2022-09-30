# Generated by Django 4.0.5 on 2022-07-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_passajir_category_passajir_gender_passajir_graj_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passajir',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Возрастная категрия'),
        ),
        migrations.AlterField(
            model_name='passajir',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='passajir',
            name='graj_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Граж. id'),
        ),
    ]

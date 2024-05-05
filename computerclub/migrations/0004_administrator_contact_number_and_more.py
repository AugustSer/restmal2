# Generated by Django 4.2.8 on 2024-03-03 08:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerclub', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='contact_number',
            field=models.IntegerField(default=79001112233, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='years_old',
            field=models.IntegerField(default=16, validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(100)], verbose_name='Лет'),
        ),
        migrations.AlterField(
            model_name='director',
            name='job_title',
            field=models.CharField(choices=[('Chief', 'Начальник'), ('Manager', 'Руководитель')], max_length=150, verbose_name='Должность'),
        ),
    ]
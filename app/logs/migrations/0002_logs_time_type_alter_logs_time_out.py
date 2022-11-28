# Generated by Django 4.0.1 on 2022-11-27 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='time_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='time_type'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='time_out',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='time_out'),
        ),
    ]
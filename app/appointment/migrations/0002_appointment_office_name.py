# Generated by Django 4.0.1 on 2022-11-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='office_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='office_name'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-11-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_barangay_user_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_checked',
            field=models.BooleanField(default=True, verbose_name='is_checked'),
        ),
    ]
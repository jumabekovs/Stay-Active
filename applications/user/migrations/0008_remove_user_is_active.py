# Generated by Django 3.1.6 on 2021-03-12 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210312_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
    ]
# Generated by Django 3.1.6 on 2021-03-15 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='default_profile.png', upload_to='profile_images'),
        ),
    ]

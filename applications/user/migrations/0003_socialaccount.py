# Generated by Django 3.1.6 on 2021-03-10 22:09

import allauth.socialaccount.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210311_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(choices=[('google', 'Google'), ('facebook', 'Facebook')], max_length=30, verbose_name='provider')),
                ('uid', models.CharField(max_length=191, verbose_name='uid')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('extra_data', allauth.socialaccount.fields.JSONField(default=dict, verbose_name='extra data')),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'social account',
                'verbose_name_plural': 'social accounts',
                'unique_together': {('provider', 'uid')},
            },
        ),
    ]
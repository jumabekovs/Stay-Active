# Generated by Django 3.1.6 on 2021-03-10 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('birthday', models.DateField(blank=True, default=datetime.date.today)),
                ('phone', models.CharField(blank=True, help_text='Contact phone number', max_length=14, null=True)),
                ('age', models.PositiveIntegerField(default=18)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('NS', 'Not Specified')], default='NS', max_length=2)),
                ('photo', models.ImageField(blank=True, default=' default_profile.png', null=True, upload_to='profile_images')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('activation_code', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

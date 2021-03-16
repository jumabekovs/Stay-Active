# Generated by Django 3.1.6 on 2021-03-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20210315_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='address_en',
            field=models.CharField(max_length=400, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='club',
            name='address_ky',
            field=models.CharField(max_length=400, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='club',
            name='address_ru',
            field=models.CharField(max_length=400, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='club',
            name='area_en',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='area_ky',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='area_ru',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='description_ky',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='gender_segregation_en',
            field=models.CharField(choices=[('men', 'Only for Men'), ('women', 'Only for Women'), ('both', 'Open')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='gender_segregation_ky',
            field=models.CharField(choices=[('men', 'Only for Men'), ('women', 'Only for Women'), ('both', 'Open')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='gender_segregation_ru',
            field=models.CharField(choices=[('men', 'Only for Men'), ('women', 'Only for Women'), ('both', 'Open')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='name_ky',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='phone_en',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='phone_ky',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='phone_ru',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=14, null=True),
        ),
    ]
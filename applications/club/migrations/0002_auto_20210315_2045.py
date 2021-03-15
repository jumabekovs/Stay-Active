# Generated by Django 3.1.6 on 2021-03-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='club',
            name='type',
        ),
        migrations.AddField(
            model_name='club',
            name='type',
            field=models.ManyToManyField(related_name='club_types', to='category.CategoryClub', verbose_name='club_types'),
        ),
    ]

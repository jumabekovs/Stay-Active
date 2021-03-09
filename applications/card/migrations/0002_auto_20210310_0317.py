# Generated by Django 3.1.6 on 2021-03-09 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Offer',
            new_name='Card',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='card.card')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

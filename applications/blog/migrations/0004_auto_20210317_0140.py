# Generated by Django 3.1.6 on 2021-03-16 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210317_0140'),
        ('blog', '0003_auto_20210315_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendpost',
            name='header_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='extendpost',
            name='header_ky',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='extendpost',
            name='header_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='extendpost',
            name='images_en',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.AddField(
            model_name='extendpost',
            name='images_ky',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.AddField(
            model_name='extendpost',
            name='images_ru',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.AddField(
            model_name='extendpost',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='extendpost',
            name='text_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='extendpost',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='blogger_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_posts', to='blog.authorpost'),
        ),
        migrations.AddField(
            model_name='post',
            name='blogger_ky',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_posts', to='blog.authorpost'),
        ),
        migrations.AddField(
            model_name='post',
            name='blogger_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_posts', to='blog.authorpost'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created_date_en',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created_date_ky',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created_date_ru',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_en',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_ky',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_ru',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.AddField(
            model_name='post',
            name='sub_title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sub_title_ky',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sub_title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='post_category', to='category.categorypost'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ky',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='post_category', to='category.categorypost'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='post_category', to='category.categorypost'),
        ),
    ]

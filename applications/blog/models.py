from django.db import models
from applications.category.models import CategoryPost


class Post(models.Model):
    title = models.ForeignKey(CategoryPost, related_name='post_category', on_delete=models.DO_NOTHING)
    sub_title = models.CharField(max_length=100)
    image = models.ImageField(max_length=1000, upload_to='post_images', blank=True, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.image:
            return self.image.url
        return ''

    def __str__(self):
        return f'{self.title}-{self.sub_title}'


class ExtendPost(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    header = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    images = models.ImageField(upload_to='post_images', blank=True, null=True)

    def __str__(self):
        return f'{self.header}'



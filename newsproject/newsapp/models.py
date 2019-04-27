from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    word = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.word


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.subject


class Post(models.Model):
    STATUS_CHOICES = (
        ('unpublished', 'Unpublished'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    update_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='unpublished')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)

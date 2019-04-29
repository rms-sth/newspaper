# Generated by Django 2.1.7 on 2019-04-29 09:17

from django.db import migrations, models
import newsapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0008_post_post_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=newsapp.models.get_image_filename, verbose_name='Image')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

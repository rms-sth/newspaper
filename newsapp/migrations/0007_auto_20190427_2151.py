# Generated by Django 2.1.7 on 2019-04-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0006_auto_20190427_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_images/%Y/%m/%d'),
        ),
    ]
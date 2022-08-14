# Generated by Django 2.1.7 on 2019-04-29 09:30

from django.db import migrations, models
import django.db.models.deletion
import newsapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("newsapp", "0009_album"),
    ]

    operations = [
        migrations.CreateModel(
            name="Images",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to=newsapp.models.get_image_filename,
                        verbose_name="Image",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="album",
            name="image",
        ),
        migrations.AddField(
            model_name="images",
            name="album",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="newsapp.Album"
            ),
        ),
    ]

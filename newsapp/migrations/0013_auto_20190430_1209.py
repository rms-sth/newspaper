# Generated by Django 2.1.7 on 2019-04-30 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsapp", "0012_remove_images_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
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
                ("title", models.CharField(blank=True, max_length=255)),
                ("file", models.FileField(upload_to="photos/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="images",
            name="album",
        ),
        migrations.DeleteModel(
            name="Album",
        ),
        migrations.DeleteModel(
            name="Images",
        ),
    ]

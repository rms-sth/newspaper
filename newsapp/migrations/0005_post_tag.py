# Generated by Django 2.1.7 on 2019-04-25 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsapp", "0004_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(to="newsapp.Tag"),
        ),
    ]

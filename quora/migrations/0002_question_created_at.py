# Generated by Django 4.2.3 on 2025-04-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quora", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]

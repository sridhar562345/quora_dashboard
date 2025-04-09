# Generated by Django 4.2.3 on 2025-04-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quora", "0002_question_created_at"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="like",
            constraint=models.UniqueConstraint(
                fields=("answer", "user"), name="unique_like"
            ),
        ),
    ]

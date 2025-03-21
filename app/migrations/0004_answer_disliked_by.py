# Generated by Django 5.1.5 on 2025-01-22 14:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_answer_liked_by_answer_likes_count'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='disliked_by',
            field=models.ManyToManyField(blank=True, related_name='disliked_answers', to=settings.AUTH_USER_MODEL),
        ),
    ]

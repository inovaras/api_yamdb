# Generated by Django 3.2 on 2023-05-11 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_title_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
    ]

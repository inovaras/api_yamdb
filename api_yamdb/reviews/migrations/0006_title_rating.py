# Generated by Django 3.2 on 2023-05-11 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_remove_title_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
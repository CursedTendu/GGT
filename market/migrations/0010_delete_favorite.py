# Generated by Django 4.2.3 on 2023-07-26 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_favorite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
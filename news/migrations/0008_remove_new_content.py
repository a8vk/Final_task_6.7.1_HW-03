# Generated by Django 4.2 on 2023-04-25 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_remove_new_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='content',
        ),
    ]

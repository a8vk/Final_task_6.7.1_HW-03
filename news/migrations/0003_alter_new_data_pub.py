# Generated by Django 4.2 on 2023-04-15 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_new_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='data_pub',
            field=models.DateField(auto_now_add=True),
        ),
    ]

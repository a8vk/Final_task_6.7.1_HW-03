# Generated by Django 4.2 on 2023-04-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoprj', '0002_alter_category_options_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
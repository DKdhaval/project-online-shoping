# Generated by Django 4.2 on 2023-06-03 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Description',
            field=models.TextField(),
        ),
    ]

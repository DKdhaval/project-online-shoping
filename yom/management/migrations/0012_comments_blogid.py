# Generated by Django 4.2 on 2023-06-06 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='Blogid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='management.blog'),
        ),
    ]

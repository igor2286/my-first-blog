# Generated by Django 3.1.2 on 2020-11-07 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_commentpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentpost',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 3.2.12 on 2023-10-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
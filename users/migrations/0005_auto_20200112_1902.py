# Generated by Django 2.2.5 on 2020-01-12 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200112_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='currrency',
            new_name='currency',
        ),
    ]

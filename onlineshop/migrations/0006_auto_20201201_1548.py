# Generated by Django 3.1.2 on 2020-12-01 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0005_auto_20201201_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='List',
            new_name='name',
        ),
    ]
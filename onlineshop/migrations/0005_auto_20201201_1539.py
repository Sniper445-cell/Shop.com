# Generated by Django 3.1.2 on 2020-12-01 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0004_auto_20201130_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('List', models.CharField(choices=[('Clothes', 'Clothes'), ('Accessory', 'Accessory'), ('Food', 'Food')], max_length=200, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlineshop.product')),
            ],
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]

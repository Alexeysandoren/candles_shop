# Generated by Django 3.0 on 2023-03-17 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='second_name',
            new_name='last_name',
        ),
    ]
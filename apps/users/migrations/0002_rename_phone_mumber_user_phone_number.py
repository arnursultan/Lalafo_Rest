# Generated by Django 4.2 on 2023-05-04 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_mumber',
            new_name='phone_number',
        ),
    ]
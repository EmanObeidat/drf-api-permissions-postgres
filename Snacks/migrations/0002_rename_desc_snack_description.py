# Generated by Django 4.2 on 2023-07-25 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='desc',
            new_name='description',
        ),
    ]

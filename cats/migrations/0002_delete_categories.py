# Generated by Django 4.2.4 on 2023-08-23 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
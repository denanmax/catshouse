# Generated by Django 4.2.4 on 2023-08-23 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0005_alter_cat_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Порода', 'verbose_name_plural': 'Породы'},
        ),
        migrations.AlterField(
            model_name='cat',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cats/', verbose_name='Фото'),
        ),
    ]

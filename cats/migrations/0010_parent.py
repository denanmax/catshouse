# Generated by Django 4.2.4 on 2023-09-05 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0009_alter_categories_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('birth_day', models.DateField(auto_now_add=True, null=True, verbose_name='Дата рождения')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.cat')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.categories', verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'предок',
                'verbose_name_plural': 'предки',
            },
        ),
    ]

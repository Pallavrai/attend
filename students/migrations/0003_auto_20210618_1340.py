# Generated by Django 3.0.7 on 2021-06-18 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20210618_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='date',
            field=models.DateField(),
        ),
    ]

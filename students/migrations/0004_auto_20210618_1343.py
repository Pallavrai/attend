# Generated by Django 3.0.7 on 2021-06-18 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20210618_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='date',
            field=models.DateField(default=datetime.date(2021, 6, 18)),
        ),
    ]
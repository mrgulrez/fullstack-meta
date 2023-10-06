# Generated by Django 4.2.6 on 2023-10-05 21:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_book_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date',
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(db_column='published_date', default=datetime.datetime.now),
        ),
    ]
# Generated by Django 4.2.6 on 2023-10-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateField(db_column='date', default='2023-10-06'),
        ),
    ]

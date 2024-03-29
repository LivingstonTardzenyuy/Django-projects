# Generated by Django 4.1.5 on 2023-03-27 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_merge_20230323_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='current_location',
            field=models.CharField(choices=[('Bamenda', 'Bamenda'), ('Douala', 'Douala'), ('Yaounde', 'Yaounde'), ('Buea', 'Buea')], default=datetime.datetime(2023, 3, 27, 19, 46, 40, 10636, tzinfo=datetime.timezone.utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='current_location',
            field=models.CharField(choices=[('Bamenda', 'Bamenda'), ('Douala', 'Douala'), ('Yaounde', 'Yaounde'), ('Buea', 'Buea')], default='Bamenda', max_length=30),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='destination',
            field=models.CharField(choices=[('Bamenda', 'Bamenda'), ('Douala', 'Douala'), ('Yaounde', 'Yaounde'), ('Buea', 'Buea')], default='Douala', max_length=30),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='notes',
            field=models.CharField(max_length=200),
        ),
    ]

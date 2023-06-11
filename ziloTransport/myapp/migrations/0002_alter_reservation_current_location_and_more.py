# Generated by Django 4.1.6 on 2023-03-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='current_location',
            field=models.CharField(choices=[('1', 'Bamenda'), ('2', 'Douala'), ('3', 'Yaounde'), ('4', 'Buea')], default='1', max_length=30),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='destination',
            field=models.CharField(choices=[('1', 'Bamenda'), ('2', 'Douala'), ('3', 'Yaounde'), ('4', 'Buea')], default='2', max_length=30),
        ),
    ]
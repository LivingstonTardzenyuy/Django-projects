# Generated by Django 4.1.5 on 2023-04-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_manager_current_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('image', models.ImageField(default='default.jpg', upload_to='media')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]

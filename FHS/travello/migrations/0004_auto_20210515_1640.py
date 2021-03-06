# Generated by Django 3.2 on 2021-05-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='city',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='mainCenter',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='street',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]

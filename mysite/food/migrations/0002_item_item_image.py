# Generated by Django 3.0.4 on 2020-04-25 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://image.flaticon.com/icons/svg/1377/1377194.svg', max_length=500),
        ),
    ]
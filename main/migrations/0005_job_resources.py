# Generated by Django 3.2.2 on 2021-05-28 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210523_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='resources',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
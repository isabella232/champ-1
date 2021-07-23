# Generated by Django 3.2.2 on 2021-07-21 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=120)),
                ('label', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_label', models.CharField(max_length=20)),
                ('repo_name', models.CharField(max_length=50)),
                ('doi', models.CharField(max_length=30, unique=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.job')),
            ],
        ),
    ]
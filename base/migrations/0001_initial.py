# Generated by Django 3.2.15 on 2022-09-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('company_name', models.CharField(blank=True, max_length=70)),
                ('city', models.CharField(blank=True, max_length=70)),
                ('state', models.CharField(blank=True, max_length=70)),
                ('zip', models.IntegerField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

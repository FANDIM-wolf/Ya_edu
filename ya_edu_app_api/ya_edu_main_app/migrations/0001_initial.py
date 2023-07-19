# Generated by Django 4.1.7 on 2023-07-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('status_exist', models.BooleanField()),
                ('amount_of_users', models.IntegerField(verbose_name=1000)),
                ('phone_of_admin', models.CharField(max_length=11)),
                ('location', models.CharField(max_length=50)),
                ('date_of_start_request', models.DateField()),
                ('date_of_end_request', models.DateField()),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User_app',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=70)),
                ('region', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('field_of_study', models.CharField(max_length=200)),
                ('phone_of_user', models.CharField(max_length=11)),
                ('email_of_user', models.EmailField(max_length=254)),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-07-20 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ya_edu_main_app', '0007_token_and_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_image', models.CharField(max_length=50)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ya_edu_main_app.event')),
            ],
        ),
    ]
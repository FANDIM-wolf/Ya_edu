# Generated by Django 4.1.7 on 2023-07-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ya_edu_main_app', '0008_eventimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventimage',
            name='image',
            field=models.ImageField(default='nothing', upload_to='images'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.7 on 2023-07-20 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ya_edu_main_app', '0006_eventuser_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token_and_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=450)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ya_edu_main_app.user_app')),
            ],
        ),
    ]
# Generated by Django 4.1.9 on 2023-06-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_signup_isloggedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]

# Generated by Django 4.0 on 2023-08-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_chat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Information',
        ),
        migrations.AddField(
            model_name='signup',
            name='full_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
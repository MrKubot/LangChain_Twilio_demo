# Generated by Django 5.1.5 on 2025-01-30 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smslog',
            name='error_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]

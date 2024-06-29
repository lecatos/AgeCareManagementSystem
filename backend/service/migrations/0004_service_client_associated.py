# Generated by Django 5.0.3 on 2024-05-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_avatar'),
        ('service', '0003_alter_service_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='client_associated',
            field=models.ManyToManyField(to='client.client'),
        ),
    ]
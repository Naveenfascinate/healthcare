# Generated by Django 2.0.7 on 2021-04-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenhills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpayments',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 3.0.1 on 2020-08-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0002_likesuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likesuser',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 2.0.2 on 2018-04-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='classname',
            field=models.TextField(max_length=264, null=True),
        ),
    ]

# Generated by Django 2.0.2 on 2018-04-18 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0002_post_classname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='classname',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=20000, null=True),
        ),
    ]

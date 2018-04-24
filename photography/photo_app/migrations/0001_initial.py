# Generated by Django 2.0.2 on 2018-04-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=264, unique=True)),
                ('content', models.TextField(max_length=20000)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('content', models.TextField(max_length=20000)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
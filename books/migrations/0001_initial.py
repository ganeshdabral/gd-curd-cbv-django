# Generated by Django 3.0.3 on 2020-02-25 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField(null=True, unique=True)),
                ('title', models.CharField(max_length=150, null=True)),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('author', models.CharField(max_length=150, null=True)),
                ('page', models.IntegerField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-25 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('question', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=32)),
                ('subcategory', models.CharField(max_length=50, null=True)),
                ('URL', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]

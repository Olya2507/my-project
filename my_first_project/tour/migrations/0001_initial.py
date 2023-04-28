# Generated by Django 4.1.7 on 2023-03-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=500)),
                ('description', models.TextField()),
                ('service', models.TextField()),
                ('image', models.FileField(upload_to='img/')),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-05-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application8', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_on',)},
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_scrap_scrap_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrap',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
    ]

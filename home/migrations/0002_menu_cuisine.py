# Generated by Django 4.1.2 on 2022-10-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='cuisine',
            field=models.CharField(default='None', max_length=30),
        ),
    ]
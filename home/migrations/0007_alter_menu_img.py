# Generated by Django 4.1.2 on 2022-10-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_menu_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='img',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]
# Generated by Django 2.1.3 on 2019-09-25 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190925_1053'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Article',
        ),
    ]

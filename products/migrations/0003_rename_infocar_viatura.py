# Generated by Django 3.2.6 on 2021-11-26 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_chapa_infocar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Infocar',
            new_name='Viatura',
        ),
    ]
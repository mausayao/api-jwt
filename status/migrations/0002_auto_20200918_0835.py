# Generated by Django 3.1.1 on 2020-09-18 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['id'], 'verbose_name': 'Status post', 'verbose_name_plural': 'Status posts'},
        ),
    ]

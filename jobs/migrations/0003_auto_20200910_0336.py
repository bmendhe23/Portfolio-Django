# Generated by Django 2.2.16 on 2020-09-09 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200910_0336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imagefun',
            new_name='image',
        ),
    ]

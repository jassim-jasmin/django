# Generated by Django 3.0.2 on 2020-01-10 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datafetch_locator', '0002_auto_20200110_0723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='layer',
            old_name='question_text',
            new_name='layer_name',
        ),
    ]

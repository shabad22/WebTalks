# Generated by Django 3.0.6 on 2020-05-11 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200511_1313'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostComment',
        ),
    ]

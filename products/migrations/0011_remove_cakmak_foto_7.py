# Generated by Django 3.1.4 on 2021-04-10 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210410_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cakmak',
            name='foto_7',
        ),
    ]
# Generated by Django 3.2 on 2021-04-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20210411_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakmak',
            name='ana_foto',
            field=models.ImageField(upload_to='fotolar/%Y/%m/%d/'),
        ),
    ]
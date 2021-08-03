# Generated by Django 3.1.4 on 2021-04-05 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cakmak',
            fields=[
                ('marka', models.CharField(blank=True, max_length=200)),
                ('model', models.CharField(blank=True, max_length=200)),
                ('no', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]

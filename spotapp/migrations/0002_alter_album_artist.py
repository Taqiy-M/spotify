# Generated by Django 4.1.1 on 2022-10-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ManyToManyField(blank=True, null=True, to='spotapp.artist'),
        ),
    ]

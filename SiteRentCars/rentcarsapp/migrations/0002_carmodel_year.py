# Generated by Django 4.1 on 2022-08-11 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcarsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='Year',
            field=models.IntegerField(default=2000, verbose_name='Год выпуска'),
            preserve_default=False,
        ),
    ]

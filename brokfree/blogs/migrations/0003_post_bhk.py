# Generated by Django 2.0.7 on 2018-08-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20180807_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bhk',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
    ]

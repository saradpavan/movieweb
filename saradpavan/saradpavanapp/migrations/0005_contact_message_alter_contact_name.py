# Generated by Django 4.1.1 on 2022-10-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saradpavanapp', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saradpavanapp', '0003_moviefront_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]

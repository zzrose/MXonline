# Generated by Django 2.0.1 on 2018-01-23 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='banner images')),
                ('url', models.URLField(verbose_name='url')),
                ('index', models.IntegerField(default=100, verbose_name='order')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banner',
            },
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='verifycode')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('send_type', models.CharField(choices=[('register', 'register'), ('forget', 'forget')], max_length=10)),
                ('send_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'email verifycode',
                'verbose_name_plural': 'email verifycode',
            },
        ),
    ]

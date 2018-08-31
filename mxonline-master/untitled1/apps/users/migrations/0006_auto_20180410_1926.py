# Generated by Django 2.0.3 on 2018-04-10 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180410_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', 'register'), ('forget', 'forget'), ('update_email', 'update email')], max_length=20, verbose_name='sending type'),
        ),
    ]

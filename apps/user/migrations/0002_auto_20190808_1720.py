# Generated by Django 2.2.4 on 2019-08-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/avatar/', verbose_name='用户头像'),
        ),
    ]
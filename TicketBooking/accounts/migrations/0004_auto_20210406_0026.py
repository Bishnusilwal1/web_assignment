# Generated by Django 3.1.6 on 2021-04-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210403_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.FileField(blank=True, default='avatar.jpg', null=True, upload_to='images'),
        ),
    ]
# Generated by Django 3.1.6 on 2021-03-05 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0007_auto_20210305_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-07 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0012_auto_20210305_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(choices=[('Action', 'ACTION'), ('Comedy', 'COMEDY'), ('Drama', 'DRAMA'), ('Horror', 'HORROR'), ('Romance', 'ROMANCE'), ('Thriller', 'THRILLER')], max_length=200),
        ),
    ]
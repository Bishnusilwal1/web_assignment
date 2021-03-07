# Generated by Django 3.1.6 on 2021-03-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0011_auto_20210305_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='cast_name',
            field=models.ManyToManyField(to='Ticket.Movie'),
        ),
        migrations.AddField(
            model_name='director',
            name='director_name',
            field=models.ManyToManyField(to='Ticket.Movie'),
        ),
    ]
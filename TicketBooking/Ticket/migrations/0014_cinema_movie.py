# Generated by Django 3.1.6 on 2021-04-05 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
        ('Ticket', '0013_ticket_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='movie',
            field=models.ManyToManyField(to='cinema.Movie'),
        ),
    ]
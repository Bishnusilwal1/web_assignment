# Generated by Django 3.1.6 on 2021-04-05 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0014_cinema_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='end_start_time',
            new_name='show_end_time',
        ),
    ]
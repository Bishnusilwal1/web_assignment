# Generated by Django 3.1.6 on 2021-04-05 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
        ('Ticket', '0010_auto_20210330_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cinema.movie'),
        ),
    ]

# Generated by Django 3.1.2 on 2021-01-19 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0015_matchpt_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchpt',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamers.game'),
        ),
    ]

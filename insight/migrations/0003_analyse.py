# Generated by Django 3.1 on 2020-09-02 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0002_remove_opening_fen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analyse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turnover_move', models.IntegerField(default=0)),
                ('turnover_evaluation', models.IntegerField(default=0)),
                ('unbalance_material', models.IntegerField(default=0)),
                ('unbalance_officers', models.IntegerField(default=0)),
                ('unbalance_exchange', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insight.game')),
            ],
        ),
    ]

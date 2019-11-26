# Generated by Django 2.2.6 on 2019-11-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_move_pop_start_up'),
    ]

    operations = [
        migrations.CreateModel(
            name='stay_pop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdnm', models.CharField(max_length=20)),
                ('all_total', models.IntegerField()),
                ('men_total', models.IntegerField()),
                ('women_total', models.IntegerField()),
                ('total_20s', models.IntegerField()),
                ('total_30s', models.IntegerField()),
                ('total_40s', models.IntegerField()),
                ('total_50s', models.IntegerField()),
                ('total_60s', models.IntegerField()),
                ('men_20s', models.IntegerField()),
                ('men_30s', models.IntegerField()),
                ('men_40s', models.IntegerField()),
                ('men_50s', models.IntegerField()),
                ('men_60s', models.IntegerField()),
                ('women_20s', models.IntegerField()),
                ('women_30s', models.IntegerField()),
                ('women_40s', models.IntegerField()),
                ('women_50s', models.IntegerField()),
                ('women_60s', models.IntegerField()),
            ],
        ),
    ]

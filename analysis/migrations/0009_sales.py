# Generated by Django 2.2.7 on 2019-12-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0008_movepop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdnm', models.CharField(max_length=20)),
                ('store_code', models.CharField(max_length=20)),
                ('mon_sales', models.IntegerField()),
                ('mon_sales_count', models.IntegerField()),
                ('weekdays_sales_rate', models.IntegerField()),
                ('weekend_sales_rate', models.IntegerField()),
                ('weekdays_sales_coount', models.IntegerField()),
                ('weekend_sales_count', models.IntegerField()),
                ('breakfast_sales', models.IntegerField()),
                ('lunch_sales', models.IntegerField()),
                ('dinner_sales', models.IntegerField()),
                ('men_sales_rate', models.IntegerField()),
                ('women_sales_rate', models.IntegerField()),
            ],
        ),
    ]
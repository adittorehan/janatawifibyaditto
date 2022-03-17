# Generated by Django 4.0.3 on 2022-03-11 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmarketapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockdata',
            old_name='date',
            new_name='_date',
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='_date',
            field=models.DateField(db_column='date'),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='trade_code',
            field=models.CharField(max_length=25),
        ),
    ]
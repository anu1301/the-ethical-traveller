# Generated by Django 3.2.15 on 2023-04-03 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holiday', '0002_auto_20230327_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='booking',
            name='duration',
            field=models.IntegerField(choices=[(7, '7 Days'), (14, '14 Days'), (21, '21 Days')], default=7),
        ),
    ]

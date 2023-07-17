# Generated by Django 4.2.3 on 2023-07-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0004_statistics_cpc_statistics_cpm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.5, max_digits=10, null=True),
        ),
    ]
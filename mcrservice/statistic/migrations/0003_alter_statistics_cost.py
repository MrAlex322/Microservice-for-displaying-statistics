# Generated by Django 4.2.3 on 2023-07-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0002_alter_statistics_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.5, max_digits=10),
        ),
    ]

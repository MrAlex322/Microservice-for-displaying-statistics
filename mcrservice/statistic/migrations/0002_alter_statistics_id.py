# Generated by Django 4.2.3 on 2023-07-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
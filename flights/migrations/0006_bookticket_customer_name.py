# Generated by Django 2.1.15 on 2022-12-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_auto_20221230_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookticket',
            name='customer_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0026_sellitem_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sellitem',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

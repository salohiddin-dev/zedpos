# Generated by Django 4.2 on 2023-05-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.IntegerField(null=True),
        ),
    ]

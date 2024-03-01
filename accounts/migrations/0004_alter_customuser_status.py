# Generated by Django 4.2.4 on 2023-09-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')], default='Unpaid', max_length=100),
        ),
    ]

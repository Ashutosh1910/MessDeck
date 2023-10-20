# Generated by Django 4.2.6 on 2023-10-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_wallet_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='money',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]

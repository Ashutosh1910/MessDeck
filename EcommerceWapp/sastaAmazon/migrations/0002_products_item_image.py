# Generated by Django 4.2.6 on 2023-10-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sastaAmazon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='item_image',
            field=models.ImageField(default='img1.png', upload_to='images'),
        ),
    ]

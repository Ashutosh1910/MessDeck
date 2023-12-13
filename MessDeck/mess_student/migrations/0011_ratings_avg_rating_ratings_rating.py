# Generated by Django 4.2.7 on 2023-11-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess_student', '0010_review_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='avg_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='ratings',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

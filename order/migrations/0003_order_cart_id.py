# Generated by Django 2.2.6 on 2020-02-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.2 on 2023-08-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anbar', '0003_product_damaged_date_product_exported_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_count',
            field=models.IntegerField(default=0),
        ),
    ]

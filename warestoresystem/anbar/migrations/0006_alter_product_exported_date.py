# Generated by Django 4.2.2 on 2023-08-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anbar', '0005_alter_product_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='exported_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

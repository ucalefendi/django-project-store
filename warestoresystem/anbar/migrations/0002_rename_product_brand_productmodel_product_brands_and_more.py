# Generated by Django 4.2.2 on 2023-07-25 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anbar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='product_brand',
            new_name='product_brands',
        ),
        migrations.RemoveField(
            model_name='product',
            name='company',
        ),
        migrations.AddField(
            model_name='product',
            name='product_brands',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anbar.productbrand'),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_service', '0006_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='media/product'),
        ),
    ]
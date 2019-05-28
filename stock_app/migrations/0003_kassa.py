# Generated by Django 2.2.1 on 2019-05-27 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_app', '0002_product_selling_price'),
        ('stock_app', '0002_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kassa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.Product')),
            ],
        ),
    ]

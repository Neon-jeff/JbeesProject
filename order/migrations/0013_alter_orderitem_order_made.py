# Generated by Django 4.1.5 on 2023-02-04 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_alter_orderitem_order_made'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order_made',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_name', to='order.order'),
        ),
    ]

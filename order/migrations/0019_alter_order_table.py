# Generated by Django 4.1.5 on 2023-06-28 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0018_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.table'),
        ),
    ]

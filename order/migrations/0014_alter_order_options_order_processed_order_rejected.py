# Generated by Django 4.1.5 on 2023-05-29 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_orderitem_order_made'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='order',
            name='processed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.1.5 on 2023-06-22 17:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_remove_menuitem_image_remove_menuitem_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]

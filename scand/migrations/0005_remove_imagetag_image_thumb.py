# Generated by Django 2.1.3 on 2019-01-28 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scand', '0004_imagetag_image_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagetag',
            name='image_thumb',
        ),
    ]

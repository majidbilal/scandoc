# Generated by Django 2.1.3 on 2019-01-28 08:16

from django.db import migrations, models
import scand.models


class Migration(migrations.Migration):

    dependencies = [
        ('scand', '0003_auto_20190109_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagetag',
            name='image_thumb',
            field=models.ImageField(blank=True, null=True, upload_to=scand.models.ImageTag.get_upload_path),
        ),
    ]

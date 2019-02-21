# Generated by Django 2.1.3 on 2019-02-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scand', '0018_imagetag_is_reverted'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagetag',
            name='is_forwarded',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='is_reverted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
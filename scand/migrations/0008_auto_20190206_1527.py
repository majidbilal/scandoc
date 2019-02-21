# Generated by Django 2.1.3 on 2019-02-06 10:27

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('scand', '0007_auto_20190206_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetag',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='scand.LowerCaseTaggedItem', to='scand.LowerCaseTag', verbose_name='Tags'),
        ),
    ]
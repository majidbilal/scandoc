# Generated by Django 2.1.3 on 2019-01-09 08:47

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('scand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagetag',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='accoff',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='attr1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='attr2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='attr3',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='attr4',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='attr5',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='company',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='docref',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='pagenum',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='pernum',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='refnum',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='section',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='imagetag',
            name='years',
            field=models.CharField(blank=True, max_length=9),
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0006_auto_20200607_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Design',
            new_name='design',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Usability',
            new_name='usability',
        ),
        migrations.AddField(
            model_name='review',
            name='content_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='design_average',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='usability_average',
            field=models.FloatField(blank=True, default=0),
        ),
    ]

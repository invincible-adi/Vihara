# Generated by Django 3.2.4 on 2023-09-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20230920_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_add',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_des',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_e',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_mail',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_mob',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_org',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_phn',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_s',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

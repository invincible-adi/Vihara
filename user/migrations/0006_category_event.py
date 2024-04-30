# Generated by Django 3.2.4 on 2023-09-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200, null=True)),
                ('cpic', models.ImageField(null=True, upload_to='static/category/')),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_picture', models.ImageField(null=True, upload_to='static/event/')),
                ('price', models.IntegerField()),
                ('dprice', models.IntegerField()),
                ('event_date', models.DateField()),
                ('event_time', models.DateField()),
                ('event_detail', models.TextField(null=True)),
            ],
        ),
    ]

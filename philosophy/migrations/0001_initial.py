# Generated by Django 3.0.5 on 2020-04-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Philosophy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speech', models.TextField()),
                ('youtube_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]

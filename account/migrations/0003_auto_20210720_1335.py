# Generated by Django 3.2.3 on 2021-07-20 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210720_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'ordering': ('-mod_date',), 'verbose_name': 'community', 'verbose_name_plural': 'communitys'},
        ),
        migrations.AlterModelTable(
            name='community',
            table='community_posts',
        ),
    ]

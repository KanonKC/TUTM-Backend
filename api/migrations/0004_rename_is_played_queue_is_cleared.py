# Generated by Django 4.1.2 on 2023-03-08 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_queue_channel_title_alter_queue_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queue',
            old_name='is_played',
            new_name='is_cleared',
        ),
    ]
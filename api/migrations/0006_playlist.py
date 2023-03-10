# Generated by Django 4.1.2 on 2023-03-12 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_queue_played_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('current_queue_id', models.ForeignKey(db_column='current_queue_id', on_delete=django.db.models.deletion.CASCADE, to='api.queue')),
            ],
        ),
    ]

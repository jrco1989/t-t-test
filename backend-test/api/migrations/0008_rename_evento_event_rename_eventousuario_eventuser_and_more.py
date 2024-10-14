# Generated by Django 5.0.6 on 2024-10-14 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_evento_comment_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Evento',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='EventoUsuario',
            new_name='EventUser',
        ),
        migrations.RenameField(
            model_name='eventuser',
            old_name='evento',
            new_name='event',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='evento',
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Event', to='api.event'),
            preserve_default=False,
        ),
    ]

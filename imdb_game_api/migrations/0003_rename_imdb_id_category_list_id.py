# Generated by Django 4.1 on 2022-08-18 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_game_api', '0002_rename_list_id_category_imdb_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='imdb_id',
            new_name='list_id',
        ),
    ]

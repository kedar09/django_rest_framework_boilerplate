# Generated by Django 3.1.4 on 2021-02-01 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_and_author', '0042_auto_20210201_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author_id',
            new_name='author',
        ),
    ]

# Generated by Django 3.1.4 on 2021-02-01 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_and_author', '0043_auto_20210201_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
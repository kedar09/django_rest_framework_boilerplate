# Generated by Django 3.1.4 on 2021-02-02 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_and_author', '0046_auto_20210202_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authors',
            new_name='author_id',
        ),
    ]
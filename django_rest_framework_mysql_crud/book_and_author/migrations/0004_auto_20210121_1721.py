# Generated by Django 3.1.4 on 2021-01-21 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_and_author', '0003_auto_20210120_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='book_and_author.author'),
        ),
    ]
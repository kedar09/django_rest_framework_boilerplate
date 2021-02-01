# Generated by Django 3.1.4 on 2021-01-28 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_and_author', '0018_auto_20210127_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='book_and_author.author'),
        ),
    ]

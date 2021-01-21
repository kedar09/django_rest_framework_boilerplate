# Generated by Django 3.1.4 on 2021-01-21 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_and_author', '0006_auto_20210121_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='book_and_author.author'),
        ),
    ]

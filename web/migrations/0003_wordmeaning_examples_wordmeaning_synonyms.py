# Generated by Django 4.2.2 on 2023-06-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_wordmeaning_example_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordmeaning',
            name='examples',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wordmeaning',
            name='synonyms',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-11 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0004_personalbookmark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalbookmark',
            name='bookmark_ptr',
        ),
        migrations.RemoveField(
            model_name='personalbookmark',
            name='user',
        ),
        migrations.DeleteModel(
            name='PersonalBookmark',
        ),
    ]

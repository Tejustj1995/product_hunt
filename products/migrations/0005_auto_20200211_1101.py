# Generated by Django 3.0.3 on 2020-02-11 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200211_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='vote_total',
            new_name='votes_total',
        ),
    ]

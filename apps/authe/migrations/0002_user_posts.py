# Generated by Django 4.2.3 on 2023-08-01 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('authe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts',
            field=models.ManyToManyField(related_name='users', to='posts.product'),
        ),
    ]
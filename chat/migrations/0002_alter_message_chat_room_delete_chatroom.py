# Generated by Django 4.2 on 2023-04-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='chat_room',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
    ]

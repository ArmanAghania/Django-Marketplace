# Generated by Django 4.2 on 2023-04-11 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("conversation", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="conversationmessage",
            old_name="conent",
            new_name="content",
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='reply_body',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

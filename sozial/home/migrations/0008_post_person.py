# Generated by Django 4.2.1 on 2023-05-23 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_reply_reply_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
    ]
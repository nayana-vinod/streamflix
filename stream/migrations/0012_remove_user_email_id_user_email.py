# Generated by Django 4.0.1 on 2022-02-22 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0011_rename_email_user_email_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_id',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='stream.userdetails'),
        ),
    ]

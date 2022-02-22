# Generated by Django 4.0.1 on 2022-02-22 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stream', '0013_remove_userdetails_plan_delete_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('shows', models.ManyToManyField(to='stream.Show')),
            ],
        ),
    ]

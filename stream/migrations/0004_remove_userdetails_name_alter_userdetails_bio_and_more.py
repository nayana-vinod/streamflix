# Generated by Django 4.0.1 on 2022-02-20 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0003_production_created_year_production_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='name',
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stream.user'),
        ),
    ]
# Generated by Django 3.2.7 on 2021-09-18 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='main.memberadmin'),
        ),
    ]

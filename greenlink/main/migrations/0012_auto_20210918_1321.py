# Generated by Django 3.2.7 on 2021-09-18 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_test_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='test',
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={},
        ),
    ]

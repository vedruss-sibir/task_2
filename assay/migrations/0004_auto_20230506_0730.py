# Generated by Django 3.2.15 on 2023-05-06 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assay', '0003_answer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='test',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
    ]
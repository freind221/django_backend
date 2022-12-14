# Generated by Django 4.1.2 on 2022-10-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='contact',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

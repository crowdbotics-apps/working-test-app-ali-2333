# Generated by Django 2.2.12 on 2020-04-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='test',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

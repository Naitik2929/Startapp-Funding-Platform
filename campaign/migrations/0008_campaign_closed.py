# Generated by Django 4.1.4 on 2023-03-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0007_campaign_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]

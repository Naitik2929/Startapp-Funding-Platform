# Generated by Django 4.1.4 on 2023-03-31 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0011_rename_image_campaign_image1_campaign_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
    ]

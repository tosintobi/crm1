# Generated by Django 3.0.5 on 2020-05-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20200502_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profilepic.png', null=True, upload_to=''),
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-01 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200430_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='none',
            new_name='note',
        ),
        migrations.AlterField(
            model_name='customers',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images.jpg', null=True, upload_to=''),
        ),
    ]
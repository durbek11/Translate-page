# Generated by Django 4.1.1 on 2022-09-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0002_remove_translatepage_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='translatepage',
            name='me',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

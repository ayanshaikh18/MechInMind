# Generated by Django 3.1.7 on 2021-03-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0004_article_uploaddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ShortDescription',
            field=models.TextField(default='short desc', max_length=50),
        ),
    ]

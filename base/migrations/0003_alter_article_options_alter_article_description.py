# Generated by Django 5.0.1 on 2024-01-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_article_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(max_length=600),
        ),
    ]

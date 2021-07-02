# Generated by Django 3.2.4 on 2021-07-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=10, verbose_name='カテゴリ名英語'),
        ),
    ]

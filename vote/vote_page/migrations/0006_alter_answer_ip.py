# Generated by Django 4.0.2 on 2022-02-05 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_page', '0005_remove_answer_user_id_answer_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ip',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
    ]

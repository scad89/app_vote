# Generated by Django 4.0.2 on 2022-02-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote_page', '0004_remove_choice_enabled_choise_alter_answer_choice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user_id',
        ),
        migrations.AddField(
            model_name='answer',
            name='ip',
            field=models.GenericIPAddressField(default='127.0.0.1', verbose_name='IP адрес'),
        ),
    ]

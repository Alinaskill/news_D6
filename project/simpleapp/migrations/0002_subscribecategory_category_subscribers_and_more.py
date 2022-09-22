# Generated by Django 4.1 on 2022-09-19 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simpleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(through='simpleapp.SubscribeCategory', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subscribecategory',
            name='categoryThrough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.category'),
        ),
        migrations.AddField(
            model_name='subscribecategory',
            name='subscriberThrough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

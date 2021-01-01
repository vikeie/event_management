# Generated by Django 3.1.4 on 2021-01-01 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateTimeField(help_text='Please use the following format: <em>YYYY-MM-DD HH:MM:SS</em>.')),
                ('num_of_attendees', models.PositiveIntegerField(blank=True, default=0)),
                ('attendees', models.ManyToManyField(blank=True, related_name='attending', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]

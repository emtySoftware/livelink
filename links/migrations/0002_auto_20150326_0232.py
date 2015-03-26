# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='links',
            name='user',
        ),
        migrations.DeleteModel(
            name='Links',
        ),
        migrations.AddField(
            model_name='user',
            name='links',
            field=models.ManyToManyField(related_name='ulinks', to='links.Link'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FruitflyPredictionMiranda',
            fields=[
            ],
            options={
                'db_table': 'Fruitfly_Prediction_Miranda',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HumanPredictionMiranda',
            fields=[
            ],
            options={
                'db_table': 'Human_Prediction_Miranda',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mirdb',
            fields=[
            ],
            options={
                'db_table': 'miRDB',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MousePredictionMiranda',
            fields=[
            ],
            options={
                'db_table': 'Mouse_Prediction_Miranda',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NematodePredictionMiranda',
            fields=[
            ],
            options={
                'db_table': 'Nematode_Prediction_Miranda',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollsChoice',
            fields=[
            ],
            options={
                'db_table': 'polls_choice',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollsQuestion',
            fields=[
            ],
            options={
                'db_table': 'polls_question',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RatPredictionMiranda',
            fields=[
            ],
            options={
                'db_table': 'Rat_Prediction_Miranda',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TarbaseV5',
            fields=[
            ],
            options={
                'db_table': 'Tarbase_V5',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]

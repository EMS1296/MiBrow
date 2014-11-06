# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class FruitflyPredictionMiranda(models.Model):
    mirbase_acc = models.CharField(max_length=15, blank=True)
    mirna_name = models.CharField(max_length=15, blank=True)
    gene_id = models.IntegerField(blank=True, null=True)
    gene_symbol = models.CharField(max_length=15, blank=True)
    transcript_id = models.CharField(max_length=15, blank=True)
    ext_transcript_id = models.CharField(max_length=20, blank=True)
    mirna_alignment = models.CharField(max_length=30, blank=True)
    alignment = models.CharField(max_length=30, blank=True)
    gene_alignment = models.CharField(max_length=30, blank=True)
    mirna_start = models.IntegerField(blank=True, null=True)
    mirna_end = models.IntegerField(blank=True, null=True)
    gene_start = models.IntegerField(blank=True, null=True)
    gene_end = models.IntegerField(blank=True, null=True)
    genome_coordinates = models.CharField(max_length=40, blank=True)
    conservation = models.FloatField(blank=True, null=True)
    align_score = models.IntegerField(blank=True, null=True)
    seed_cat = models.IntegerField(blank=True, null=True)
    energy = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    mirsvr_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fruitfly_Prediction_Miranda'


class HumanPredictionMiranda(models.Model):
    mirbase_acc = models.CharField(max_length=15, blank=True)
    mirna_name = models.CharField(max_length=15, blank=True)
    gene_id = models.IntegerField(blank=True, null=True)
    gene_symbol = models.CharField(max_length=15, blank=True)
    transcript_id = models.CharField(max_length=15, blank=True)
    ext_transcript_id = models.CharField(max_length=20, blank=True)
    mirna_alignment = models.CharField(max_length=30, blank=True)
    alignment = models.CharField(max_length=30, blank=True)
    gene_alignment = models.CharField(max_length=30, blank=True)
    mirna_start = models.IntegerField(blank=True, null=True)
    mirna_end = models.IntegerField(blank=True, null=True)
    gene_start = models.IntegerField(blank=True, null=True)
    gene_end = models.IntegerField(blank=True, null=True)
    genome_coordinates = models.CharField(max_length=40, blank=True)
    conservation = models.FloatField(blank=True, null=True)
    align_score = models.IntegerField(blank=True, null=True)
    seed_cat = models.IntegerField(blank=True, null=True)
    energy = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    mirsur_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Human_Prediction_Miranda'


class MousePredictionMiranda(models.Model):
    mirbase_acc = models.CharField(max_length=15, blank=True)
    mirna_name = models.CharField(max_length=15, blank=True)
    gene_id = models.IntegerField(blank=True, null=True)
    gene_symbol = models.CharField(max_length=15, blank=True)
    transcript_id = models.CharField(max_length=15, blank=True)
    ext_transcript_id = models.CharField(max_length=20, blank=True)
    mirna_alignment = models.CharField(max_length=30, blank=True)
    alignment = models.CharField(max_length=30, blank=True)
    gene_alignment = models.CharField(max_length=30, blank=True)
    mirna_start = models.IntegerField(blank=True, null=True)
    mirna_end = models.IntegerField(blank=True, null=True)
    gene_start = models.IntegerField(blank=True, null=True)
    gene_end = models.IntegerField(blank=True, null=True)
    genome_coordinates = models.CharField(max_length=40, blank=True)
    conservation = models.FloatField(blank=True, null=True)
    align_score = models.IntegerField(blank=True, null=True)
    seed_cat = models.IntegerField(blank=True, null=True)
    energy = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    mirsvr_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mouse_Prediction_Miranda'


class NematodePredictionMiranda(models.Model):
    mirbase_acc = models.CharField(max_length=15, blank=True)
    mirna_name = models.CharField(max_length=15, blank=True)
    gene_id = models.IntegerField(blank=True, null=True)
    gene_symbol = models.CharField(max_length=15, blank=True)
    transcript_id = models.CharField(max_length=15, blank=True)
    ext_transcript_id = models.CharField(max_length=20, blank=True)
    mirna_alignment = models.CharField(max_length=30, blank=True)
    alignment = models.CharField(max_length=30, blank=True)
    gene_alignment = models.CharField(max_length=30, blank=True)
    mirna_start = models.IntegerField(blank=True, null=True)
    mirna_end = models.IntegerField(blank=True, null=True)
    gene_start = models.IntegerField(blank=True, null=True)
    gene_end = models.IntegerField(blank=True, null=True)
    genome_coordinates = models.CharField(max_length=40, blank=True)
    conservation = models.FloatField(blank=True, null=True)
    align_score = models.IntegerField(blank=True, null=True)
    seed_cat = models.IntegerField(blank=True, null=True)
    energy = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    mirsvr_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Nematode_Prediction_Miranda'


class RatPredictionMiranda(models.Model):
    mirbase_acc = models.CharField(max_length=15, blank=True)
    mirna_name = models.CharField(max_length=15, blank=True)
    gene_id = models.IntegerField(blank=True, null=True)
    gene_symbol = models.CharField(max_length=15, blank=True)
    transcript_id = models.CharField(max_length=15, blank=True)
    ext_transcript_id = models.CharField(max_length=20, blank=True)
    mirna_alignment = models.CharField(max_length=30, blank=True)
    alignment = models.CharField(max_length=30, blank=True)
    gene_alignment = models.CharField(max_length=30, blank=True)
    mirna_start = models.IntegerField(blank=True, null=True)
    mirna_end = models.IntegerField(blank=True, null=True)
    gene_start = models.IntegerField(blank=True, null=True)
    gene_end = models.IntegerField(blank=True, null=True)
    genome_coordinates = models.CharField(max_length=40, blank=True)
    conservation = models.FloatField(blank=True, null=True)
    align_score = models.IntegerField(blank=True, null=True)
    seed_cat = models.IntegerField(blank=True, null=True)
    energy = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    mirsvr_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rat_Prediction_Miranda'


class TarbaseV5(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    id_v4 = models.IntegerField(blank=True, null=True)
    data_type = models.CharField(max_length=25, blank=True)
    support_type = models.CharField(max_length=8, blank=True)
    organism = models.CharField(max_length=15, blank=True)
    mirna = models.CharField(max_length=15, blank=True)
    hgnc_symbol = models.CharField(max_length=15, blank=True)
    gene = models.CharField(max_length=25, blank=True)
    isoform = models.CharField(max_length=25, blank=True)
    ensemble = models.CharField(max_length=17, blank=True)
    chr_loc = models.CharField(max_length=30, blank=True)
    mre = models.CharField(max_length=15, blank=True)
    s_s_s = models.CharField(max_length=8, blank=True)
    i_s = models.CharField(max_length=30, blank=True)
    d_s = models.CharField(max_length=30, blank=True)
    validation = models.CharField(max_length=20, blank=True)
    paper = models.CharField(max_length=30, blank=True)
    target_seq = models.CharField(max_length=30, blank=True)
    mirna_seq = models.CharField(max_length=30, blank=True)
    seq_location = models.CharField(max_length=30, blank=True)
    pmid = models.IntegerField(blank=True, null=True)
    kegg = models.CharField(db_column='KEGG', max_length=20, blank=True)  # Field name made lowercase.
    protein_type = models.CharField(max_length=20, blank=True)
    differentially_expressed_in = models.CharField(max_length=30, blank=True)
    pathology_or_event = models.CharField(max_length=30, blank=True)
    mis_regulation = models.CharField(max_length=15, blank=True)
    gene_expression = models.CharField(max_length=30, blank=True)
    tumour_involvement = models.CharField(max_length=30, blank=True)
    bib_notes = models.TextField(blank=True)
    cell_lines_used = models.CharField(max_length=30, blank=True)
    hgnc_id = models.CharField(max_length=20, blank=True)
    swissprot = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'Tarbase_V5'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Mirdb(models.Model):
    gene_name = models.CharField(max_length=15, blank=True)
    targen_name = models.CharField(max_length=20, blank=True)
    confidence_percent = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'miRDB'


class PollsChoice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion')

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'

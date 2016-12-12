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
from django.contrib.auth.models import User
from django.db import models
from django.db import connection

class AccountAccount(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField(unique=True)
    timezone = models.CharField(max_length=100)
    language = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'account_account'


class AccountAccountdeletion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=75)
    date_requested = models.DateTimeField()
    date_expunged = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_accountdeletion'


class AccountEmailaddress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    email = models.CharField(unique=True, max_length=75)
    verified = models.BooleanField()
    primary = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email_address = models.ForeignKey(AccountEmailaddress)
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AccountSignupcode(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(unique=True, max_length=64)
    max_uses = models.PositiveIntegerField()
    expiry = models.DateTimeField(blank=True, null=True)
    inviter_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=75)
    notes = models.TextField()
    sent = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField()
    use_count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'account_signupcode'


class AccountSignupcoderesult(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    signup_code = models.ForeignKey(AccountSignupcode)
    user_id = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'account_signupcoderesult'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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
    action_flag = models.PositiveSmallIntegerField()
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


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class EventlogLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    action = models.CharField(max_length=50)
    extra = models.TextField()

    class Meta:
        managed = False
        db_table = 'eventlog_log'
class JobManager(models.Manager):
    def my_custom_sql():
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM job')
        row = cursor.fetchone()
        f=open('ss.txt','w')
        for p in row:
           f.write(P)
        f.close()
        return row

class Job(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    status = models.CharField(max_length=200, blank=True)
    submitted_time = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    detail_status = models.CharField(max_length=100, blank=True)
    dareprocess_id = models.CharField(max_length=100, blank=True)
    userid = models.IntegerField(blank=True, null=True)
    objects=JobManager()
    #user=models.ForeingKey(User)
    class Meta:
        managed = True
        db_table = 'job'            
class JobManagementJob(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    job_description = models.CharField(db_column='Job_Description', max_length=200)  # Field name made lowercase.
    submitted_time = models.DateTimeField(db_column='Submitted_time')  # Field name made lowercase.
    job_status = models.DateTimeField(db_column='Job_Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'job_management_job'


class Jobinfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    description = models.CharField(max_length=200, blank=True)
    submitted_time = models.CharField(max_length=100, blank=True)
    key = models.CharField(max_length=50, blank=True)
    value = models.CharField(max_length=50, blank=True)
    jobid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobinfo'


class Shayan(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    status = models.CharField(max_length=200)
    submitted_time = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    detail_status = models.CharField(max_length=100)
    dareprocess_id = models.CharField(max_length=100)
    userid = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'shayan'


class Tool(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=200, blank=True)
    submitted_time = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    userid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tool'


class Toolinfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=200, blank=True)
    submitted_time = models.CharField(max_length=100, blank=True)
    sysytemarchitecture = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    toolpath = models.CharField(max_length=100, blank=True)
    toolid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toolinfo'


class User(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200)
    organization = models.CharField(max_length=100)
    submitted_time = models.CharField(max_length=30, blank=True)
    salt = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'user'
class FileTransfer(models.Model):
    file_list = models.CharField(max_length=100)

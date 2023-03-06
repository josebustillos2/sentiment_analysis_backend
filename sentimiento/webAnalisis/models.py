from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=1000)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    codename = models.CharField(max_length=1000)
    content_type_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    date_joined = models.DateTimeField()
    email = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=1000)
    id = models.IntegerField(primary_key=True)  # AutoField?
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    last_name = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    username = models.CharField(unique=True,max_length=1000)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    group_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    permission_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_flag = models.IntegerField()
    action_time = models.DateTimeField()
    change_message = models.CharField(max_length=1000)
    content_type_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.CharField(max_length=1000)
    object_repr = models.CharField(max_length=1000)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=1000)
    id = models.IntegerField(primary_key=True)  # AutoField?
    model = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=1000)
    applied = models.DateTimeField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    expire_date = models.DateTimeField()
    session_data = models.CharField(max_length=1000)
    session_key = models.CharField(primary_key=True, max_length=1000)

    class Meta:
        managed = False
        db_table = 'django_session'


from django.contrib.postgres.fields import JSONField

class Tuit(models.Model):
    data = JSONField()

    def __str__(self):
        return self.name
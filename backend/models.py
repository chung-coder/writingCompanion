from django.db import models
from django.contrib.auth.models import User


class Class(models.Model):
    class_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "Class"


class Diary(models.Model):
    student = models.ForeignKey("Student", models.DO_NOTHING)
    date = models.DateField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_favorite = models.IntegerField()
    last_modified_date = models.DateField()
    mood = models.CharField(max_length=50, blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    diary_type = models.CharField(max_length=50, blank=True, null=True)
    word_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = "Diary"


class Gptassistance(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    diary = models.ForeignKey(Diary, models.DO_NOTHING)
    interaction_time = models.DateTimeField()
    user_input = models.TextField()
    gpt_response = models.TextField()

    class Meta:
        managed = False
        db_table = "GPTAssistance"


class Gptinteraction(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    diary = models.ForeignKey(Diary, models.DO_NOTHING)
    interaction_time = models.DateTimeField()
    dialogue_record = models.TextField()

    class Meta:
        managed = False
        db_table = "GPTInteraction"


class Student(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    user = models.ForeignKey(User, models.DO_NOTHING)
    class_field = models.ForeignKey(
        "Class", models.DO_NOTHING, db_column="class_id", blank=True, null=True
    )  # Field renamed because it was a Python reserved word.
    teacher = models.ForeignKey("Teacher", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Student"


class Teacher(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "Teacher"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"

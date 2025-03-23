from django.db import models
from django.contrib.auth.models import User


class Class(models.Model):
    """
    Class model representing a school class
    """
    class_name = models.CharField(
        max_length=255,
        help_text="Name of the school class"
    )

    class Meta:
        db_table = "Class"

    def __str__(self):
        return self.class_name

class Teacher(models.Model):
    """
    Represents a teacher in the system.
    Contains basic information about teachers and their relationship with users.
    """
    name = models.CharField(max_length=255)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='teacher',
        help_text="User account associated with this teacher"
    )

    class Meta:
        db_table = "Teacher"

    def __str__(self):
        return self.name


class Student(models.Model):
    """
    Represents a student in the system.
    Contains student information and their relationships with teachers and classes.
    """
    name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=1,
        choices=[('M', 'Male'), ('F', 'Female')],
        help_text="Select 'M' for Male or 'F' for Female"
    )
    user = models.OneToOneField(
        User,
        null=True,
        on_delete=models.CASCADE,       # When the related User is deleted, this Student will also be deleted
        related_name='student',          # Enables reverse lookup: user.student returns the related Student
        help_text="User account associated with this student"
    )
    class_field = models.ForeignKey(
        "Class",
        on_delete=models.SET_NULL,
        db_column="class_id",
        blank=True,
        null=True,
        related_name='students',
        help_text="The class this student belongs to"
    )
    teacher = models.ForeignKey(
        "Teacher",
        on_delete=models.SET_NULL,           # If the related teacher is deleted, set this field to NULL
        blank=True,
        null=True,
        related_name='students',              # Enables reverse lookup: teacher.students returns all related students
        help_text="The teacher responsible for this student"
    )

    class Meta:
        db_table = "Student"

    def __str__(self):
        class_name = self.class_field.class_name if self.class_field else "No Class"
        return f"{self.name} - Class: {class_name}"

class Diary(models.Model):
    """
    Represents a student's diary entry.
    Stores diary content and metadata including mood, target, and word count.
    """
    MOOD_CHOICES = [
        ('very_good', 'very good'),
        ('good', 'good'),
        ('normal', 'normal'),
        ('bad', 'bad'),
        ('very_bad', 'very bad')
    ]
    TARGET_CHOICES = [
        ('self', 'self'),
        ('friend', 'friend'),
        ('family', 'family'),
        ('other', 'other')
    ]
    DIARY_TYPE_CHOICES = [
        ('Interaction', 'Interaction'),
        ('Assistance', 'Assistance')
    ]
    student = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True,
        related_name='diaries',
        db_column='student_id',
        help_text="The student who wrote this diary"
    )
    date = models.DateField(
        help_text="Date when the diary was written"
    )
    title = models.CharField(
        max_length=255,
        help_text="Title of the diary entry"
    )
    content = models.TextField(
        help_text="Main content of the diary"
    )
    is_favorite = models.BooleanField(
        default=False,
        help_text="Whether this diary is marked as favorite"
    )
    last_modified_date = models.DateField(
        auto_now=True,
        help_text="Last modification date of the diary"
    )
    mood = models.CharField(
        max_length=50,
        choices=MOOD_CHOICES,
        blank=True,
        null=True,
        help_text="Student's emotional state or feelings when writing the diary"
    )
    target = models.CharField(
        max_length=255,
        choices=TARGET_CHOICES,
        blank=True,
        null=True,
        help_text="Who the diary is written for (self, friends, family, others)"
    )
    diary_type = models.CharField(
        max_length=50,
        choices=DIARY_TYPE_CHOICES,
        blank=True,
        null=True,
        help_text="Type of diary entry: Interaction or Assistance mode with GPT"
    )
    word_count = models.IntegerField(
        default=0,
        help_text="Number of words in the diary content"
    )

    class Meta:
        db_table = "Diary"


class Gptassistance(models.Model):
    """
    Represents AI assistance provided for diary writing.
    Stores both user input and GPT's response for each assistance instance.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='gpt_assistance',
        help_text="User who requested GPT assistance"
    )
    diary = models.ForeignKey(
        Diary,
        on_delete=models.SET_NULL,
        null=True,
        related_name='gpt_assistance',
        help_text="The diary entry this assistance is related to"
    )
    interaction_time = models.DateTimeField(
        help_text="Timestamp of when the student interacted with GPT"
    )
    user_input = models.TextField(
        help_text="User's question or request for assistance"
    )
    gpt_response = models.TextField(
        help_text="GPT's response to the user's request"
    )

    class Meta:
        db_table = "GPTAssistance"
        ordering = ['-interaction_time']

    def __str__(self):
        return f"GPT assistance - {self.user.username} - {self.diary.title} - {self.interaction_time}"


class Gptinteraction(models.Model):
    """
    Represents an interaction between a user and GPT.
    Stores the complete dialogue record for each interaction.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='gpt_interactions',
        help_text="User who initiated the GPT interaction"
    )
    diary = models.ForeignKey(
        Diary,
        on_delete=models.SET_NULL,
        null=True,
        related_name='gpt_interactions',
        help_text="The diary entry this interaction is related to"
    )
    interaction_time = models.DateTimeField(
        help_text="Timestamp of when the student interacted with GPT"
    )
    dialogue_record = models.TextField(
        help_text="Complete record of the conversation with GPT"
    )

    class Meta:
        db_table = "GPTInteraction"
        ordering = ['-interaction_time']

    def __str__(self):
        return f"GPT interaction - {self.user.username} - {self.diary.title} - {self.interaction_time}"

# Django's built-in models
class DjangoContentType(models.Model):
    """
    Django's built-in content type system.
    """
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    """
    Django's migration history tracking.
    """
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    """
    Django's session management.
    """
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"

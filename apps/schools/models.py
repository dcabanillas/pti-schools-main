from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("name", "level")

    def __str__(self):
        return "{}/{}".format(self.name, self.level)


class Student(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="students", blank=True, null=True)
    groups = models.ManyToManyField(Group, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)


class Speciality(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Specialities"


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    specialities = models.ManyToManyField(Speciality, blank=True)
    photo = models.ImageField(upload_to="teachers", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)


class Status(models.TextChoices):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class SkillType(models.TextChoices):
    SOFT = "SOFT"
    HARD = "HARD"


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    skill_type = models.CharField(
        choices=SkillType.choices, default=SkillType.HARD, max_length=4, db_index=True
    )
    evaluation = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "type={} {}".format(self.skill_type, self.name)


class Document(models.Model):
    name = models.CharField(max_length=255)
    doc_file = models.FileField(upload_to="documents")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DayChoices(models.TextChoices):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class Day(models.Model):
    name = models.CharField(
        choices=DayChoices.choices,
        default=DayChoices.MONDAY,
        max_length=10,
        db_index=True,
    )

    def __str__(self):
        return self.name


class Frequency(models.TextChoices):
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"


class Schedule(models.Model):
    start_day = models.DateField()
    end_day = models.DateField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    frequency = models.CharField(
        choices=Frequency.choices,
        default=Frequency.WEEKLY,
        max_length=10,
        db_index=True,
    )
    week_days = models.ManyToManyField(Day)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "frequency={} start_day={} start_hour={} end_day={} end_hour={}".format(
            self.frequency, self.start_day, self.start_hour, self.end_day, self.end_hour
        )


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        choices=Status.choices, default=Status.ACTIVE, max_length=8, db_index=True
    )
    skills = models.ManyToManyField(Skill, blank=True)
    is_activity = models.BooleanField(default=False)
    schedules = models.ManyToManyField(Schedule, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    teachers = models.ManyToManyField(Teacher, blank=True)
    students = models.ManyToManyField(Student, blank=True)
    documents = models.ManyToManyField(Document, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} status={}".format(self.name, self.status)

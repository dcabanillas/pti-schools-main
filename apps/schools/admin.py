from django.contrib import admin
from .models import (
    Group,
    Student,
    Speciality,
    Teacher,
    Skill,
    Document,
    Day,
    Schedule,
    Project,
)


class StudentInline(admin.TabularInline):
    model = Student.groups.through


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]
    pass


admin.site.register(Group, GroupAdmin)


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)


class SpecialityAdmin(admin.ModelAdmin):
    pass


admin.site.register(Speciality, SpecialityAdmin)


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)


class SkillAdmin(admin.ModelAdmin):
    pass


admin.site.register(Skill, SkillAdmin)


class DocumentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Document, DocumentAdmin)


class DayAdmin(admin.ModelAdmin):
    pass


admin.site.register(Day, DayAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Schedule, ScheduleAdmin)


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ("students", "teachers", "schedules", "skills", "documents")
    pass


admin.site.register(Project, ProjectAdmin)

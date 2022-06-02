import json

from django.core.management.base import BaseCommand, CommandError
from schools.models import Schedule, Student, Teacher, Skill, Group, Project, Speciality


class Command(BaseCommand):
    help = "Import data from old database"

    def handle(self, *args, **options):

        results = json.load(open("students.json"))
        for r in results:
            st = Student()
            st.name = r["name"]
            st.last_name = r["last_name"]
            if r["birth_date"] != "":
                st.birth_date = r["birth_date"]
            st.save()

        results = json.load(open("teachers.json"))
        for r in results:
            sp, created = Speciality.objects.get_or_create(name=r["specialty"])

            t = Teacher()
            t.name = r["name"]
            t.last_name = r["last_name"]
            t.save()

            t.specialities.add(sp)
            t.save()

        results = json.load(open("groups.json"))
        for r in results:
            g = Group()
            g.name = r["name"]
            g.level = r["level"]
            g.save()

        results = json.load(open("projects.json"))
        for r in results:
            p = Project()
            p.name = r["name"]
            p.description = r["description"]
            p.is_activity = r["is_activity"]
            p.save()

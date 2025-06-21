from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from students.models import Student
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake students for testing'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of students to create')
        parser.add_argument('--teacher', type=str, required=True, help='Username of the teacher')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        teacher_username = kwargs['teacher']

        try:
            teacher = User.objects.get(username=teacher_username)
        except User.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"No teacher with username '{teacher_username}' found"))
            return

        subjects = ['Math', 'Science', 'English', 'History', 'Physics']

        for _ in range(count):
            name = fake.name()
            subject = random.choice(subjects)
            marks = random.randint(40, 100)

            student, created = Student.objects.get_or_create(
                teacher=teacher,
                name=name,
                subject=subject,
                defaults={'marks': marks}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Added student: {name}, {subject}, {marks}"))
            else:
                student.marks += marks
                student.save()
                self.stdout.write(self.style.WARNING(f"Updated student marks: {name}, new total = {student.marks}"))

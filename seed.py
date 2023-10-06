from datetime import date, datetime, timedelta
from random import randint, choice
from faker import Faker
from sqlalchemy import select

from models import Teacher, Student, Discipline, Grade, Group
from db_connect import session


def date_range(start: date, end: date) -> list:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


def fill_data():
    disciplines = [
        "Вища математика",
        "Статистика",
        "Фінансовий аналіз",
        "Програмування",
        "Економіка",
        "Історія України",
        "Англійська",
        "ОБЖ",
    ]

    groups = ["PD-1", "PD-2", "PD-3"]
    NUMBER_TEACHERS = 5
    NUMBER_STUDENTS = 50
    fake = Faker()

    def seed_teachers():
        for _ in range(NUMBER_TEACHERS):
            teacher = Teacher(name=fake.name())
            session.add(teacher)
        session.commit()

    def seed_disciplines():
        teacher_ids = session.scalars(select(Teacher.id)).all()
        for discipline in disciplines:
            session.add(Discipline(name=discipline, teacher_id=choice(teacher_ids)))
        session.commit()

    def seed_groups():
        for group in groups:
            session.add(Group(name=group))
        session.commit()

    def seed_students():
        group_ids = session.scalars(select(Group.id)).all()
        for _ in range(NUMBER_STUDENTS):
            student = Student(name=fake.name(), group_id=choice(group_ids))
            session.add(student)
        session.commit()

    def seed_grades():
        start_date = datetime.strptime("2023-09-01", "%Y-%m-%d")
        end_date = datetime.strptime("2024-06-30", "%Y-%m-%d")
        d_range = date_range(start=start_date, end=end_date)
        discipline_ids = session.scalars(select(Discipline.id)).all()
        student_ids = session.scalars(select(Student.id)).all()

        for d in d_range:
            random_id_discipline = choice(discipline_ids)
            random_ids_student = [choice(student_ids) for _ in range(5)]
            for student_id in random_ids_student:
                grade = Grade(
                    grade=randint(1, 12),
                    date_of_grade=d,
                    student_id=student_id,
                    discipline_id=random_id_discipline,
                )
                session.add(grade)
        session.commit()

    seed_teachers()
    seed_disciplines()
    seed_groups()
    seed_students()
    seed_grades()


if __name__ == "__main__":
    fill_data()

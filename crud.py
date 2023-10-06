from models import Teacher, Group, Student, Discipline, Grade
from db_connect import session


def create_record(model, name):
    model = model.lower()
    if model == 'teacher':
        new_teacher = Teacher(name=name)
        session.add(new_teacher)
        session.commit()
        session.close()
    elif model == 'group':
        new_group = Group(name=name)
        session.add(new_group)
    elif model == 'student':
        new_student = Student(name=name, group_id=group_id)  # Assuming group_id is provided
        session.add(new_student)
    elif model == 'discipline':
        new_discipline = Discipline(name=name, teacher_id=teacher_id)  # Assuming teacher_id is provided
        session.add(new_discipline)
    elif model == 'grade':
        new_grade = Grade(grade=grade, date_of_grade=date_of_grade, student_id=student_id, discipline_id=discipline_id)
        session.add(new_grade)
    else:
        print(f"Unknown model: {model}")


def update_record(model, _id, name):
    model = model.lower()
    if model == 'teacher':
        teacher = session.query(Teacher).filter_by(id=_id).first()
        if teacher:
            teacher.name = name
            session.commit()
            print(f"Teacher with id {_id} updated.")
        else:
            print(f"Teacher with id {_id} not found.")
    elif model == 'group':
        group = session.query(Group).filter_by(id=_id).first()
        if group:
            group.name = name
            session.commit()
            print(f"Group with id {_id} updated.")
        else:
            print(f"Group with id {_id} not found.")
    elif model == 'student':
        student = session.query(Student).filter_by(id=_id).first()
        if student:
            student.name = name
            session.commit()
            print(f"Student with id {_id} updated.")
        else:
            print(f"Student with id {_id} not found.")
    elif model == 'discipline':
        discipline = session.query(Discipline).filter_by(id=_id).first()
        if discipline:
            discipline.name = name
            session.commit()
            print(f"Discipline with id {_id} updated.")
        else:
            print(f"Discipline with id {_id} not found.")
    else:
        print(f"Unknown model: {model}")


def get_all_records(model):
    model = model.lower()
    if model == 'teacher':
        return session.query(Teacher).all()
    elif model == 'group':
        return session.query(Group).all()
    elif model == 'student':
        return session.query(Student).all()
    elif model == 'discipline':
        return session.query(Discipline).all()
    elif model == 'grade':
        return session.query(Grade).all()
    else:
        print(f"Unknown model: {model}")
        return []


def remove_record(model, _id):
    model = model.lower()
    if model == 'teacher':
        teacher = session.query(Teacher).filter_by(id=_id).first()
        if teacher:
            session.delete(teacher)
            session.commit()
            print(f"Teacher with id {_id} removed.")
        else:
            print(f"Teacher with id {_id} not found.")
    elif model == 'group':
        group = session.query(Group).filter_by(id=_id).first()
        if group:
            session.delete(group)
            session.commit()
            print(f"Group with id {_id} removed.")
        else:
            print(f"Group with id {_id} not found.")
    elif model == 'student':
        student = session.query(Student).filter_by(id=_id).first()
        if student:
            session.delete(student)
            session.commit()
            print(f"Student with id {_id} removed.")
        else:
            print(f"Student with id {_id} not found.")
    elif model == 'discipline':
        discipline = session.query(Discipline).filter_by(id=_id).first()
        if discipline:
            session.delete(discipline)
            session.commit()
            print(f"Discipline with id {_id} removed.")
        else:
            print(f"Discipline with id {_id} not found.")
    elif model == 'grade':
        grade = session.query(Grade).filter_by(id=_id).first()
        if grade:
            session.delete(grade)
            session.commit()
            print(f"Grade with id {_id} removed.")
        else:
            print(f"Grade with id {_id} not found.")
    else:
        print(f"Unknown model: {model}")


if __name__=='__main__':
    create_record('teacher', 'John Doe')
    create_record('group', 'A')
    create_record('student', 'Jane Doe', group_id=1)
    create_record('discipline', 'Math', teacher_id=1)
    create_record('grade', grade=85, date_of_grade='2023-10-04', student_id=1, discipline_id=1)

    update_record('teacher', 1, 'John Smith')
    update_record('group', 1, 'B')

    all_teachers = get_all_records('teacher')
    all_groups = get_all_records('group')

    remove_record('teacher', 1)
    remove_record('group', 2)
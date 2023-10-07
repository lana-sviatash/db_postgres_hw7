from sqlalchemy.orm.exc import NoResultFound

from models import Teacher, Group, Student, Discipline, Grade
from db_connect import session


MODELS = {
    "teacher": Teacher,
    "group": Group,
    "student": Student,
    "discipline": Discipline,
    "grade": Grade,
}


def create_record(model, **kwargs):
    model = model.lower()
    try:
        new_record = MODELS[model](**kwargs)
        session.add(new_record)
        session.commit()
        print(f"Created {model} record successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error creating {model} record:", str(e))


def list_records(model):
    model = model.lower()
    try:
        records = session.query(MODELS[model]).all()
        for record in records:
            print(record.__dict__)
    except Exception as e:
        print(f"Error listing {model} records:", str(e))


def update_record(model, id, **kwargs):
    model = model.lower()
    try:
        record = session.query(MODELS[model]).filter_by(id=id).one()
        for key, value in kwargs.items():
            setattr(record, key, value)
        session.commit()
        print(f"Updated {model} record with id {id} successfully.")
    except NoResultFound:
        print(f"No {model} record found with id {id}.")
    except Exception as e:
        session.rollback()
        print(f"Error updating {model} record:", str(e))


def remove_record(model, id):
    model = model.lower()
    try:
        record = session.query(MODELS[model]).filter_by(id=id).one()
        session.delete(record)
        session.commit()
        print(f"Removed {model} record with id {id} successfully.")
    except NoResultFound:
        print(f"No {model} record found with id {id}.")
    except Exception as e:
        session.rollback()
        print(f"Error removing {model} record:", str(e))


if __name__ == "__main__":
    create_record(model="teacher", name="John Doe")
    create_record(model="group", name="A")
    create_record(model="student", name="Jane Doe", group_id=1)
    create_record(model="discipline", name="Math", teacher_id=1)
    create_record(
        model="grade",
        grade=85,
        date_of_grade="2023-10-04",
        student_id=1,
        discipline_id=1,
    )

    update_record(model="teacher", id=1, name="John Smith")
    update_record(model="group", id=1, name="B")

    all_teachers = list_records(model="teacher")
    all_groups = list_records(model="group")

    remove_record(model="teacher", id=1)
    remove_record(model="group", id=2)

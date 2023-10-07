from sqlalchemy import func, desc, select, and_
from pprint import pprint

from models import Teacher, Student, Discipline, Grade, Group
from db_connect import session


"""SELECT s.fullname AS student, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g 
INNER JOIN students s ON s.id = g.student_id 
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 5;"""


def select_1():
    res = (
        session.query(
            Student.name, func.round(func.avg(Grade.grade), 1).label("avg_grade")
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.name)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return res


"""SELECT d.name AS discipline, s.fullname AS student, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g 
INNER JOIN students s ON s.id = g.student_id 
INNER JOIN disciplines d  ON d.id = g.discipline_id  
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 1;"""


def select_2(discipline_id):
    res = (
        session.query(
            Discipline.name,
            Student.name,
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .filter(Discipline.id == discipline_id)
        .group_by(Student.name, Discipline.name)
        .order_by(desc("avg_grade"))
        .limit(1)
        .all()
    )
    return res


"""SELECT d.name AS disciplines, s.fullname AS student, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g 
INNER JOIN students s ON s.id = g.student_id 
INNER JOIN disciplines d  ON d.id = g.discipline_id  
WHERE d.id = 1
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 5;"""


def select_3(discipline_id):
    res = (
        session.query(
            Discipline.name,
            Group.name,
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Group)
        .filter(Discipline.id == discipline_id)
        .group_by(Group.name, Discipline.name)
        .order_by(desc("avg_grade"))
        .all()
    )
    return res


"""SELECT ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g;"""


def select_4():
    res = (
        session.query(
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
        )
        .select_from(Grade)
        .all()
    )
    return res


"""SELECT t.fullname AS teacher, d.name AS discipline
FROM teachers t  
JOIN disciplines d  ON d.teacher_id = t.id  
ORDER BY t.fullname
LIMIT 5;"""


def select_5(teacher_id):
    res = (
        session.query(Teacher.name, Discipline.name)
        .select_from(Discipline)
        .join(Teacher)
        .filter(Teacher.id == teacher_id)
        .all()
    )
    return res


"""SELECT g.name AS 'group', s.fullname AS student
FROM students s  
JOIN groups g ON g.id = s.group_id  
WHERE g.id = 1
ORDER BY s.fullname
LIMIT 5;"""


def select_6(group_id):
    res = (
        session.query(Student.name, Group.name)
        .select_from(Student)
        .join(Group)
        .filter(Group.id == group_id)
        .order_by(Student.name)
        .limit(5)
        .all()
    )
    return res


"""SELECT g2.name AS 'group', d.name AS discipline, s.fullname AS student, g.grade
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN groups g2 ON g2.id = s.group_id 
JOIN disciplines d ON d.id = g.discipline_id
WHERE d.id = 1 AND g2.id = 1
ORDER BY s.fullname
LIMIT 5;"""


def select_7(group_id, discipline_id):
    res = (
        session.query(Student.name, Group.name, Discipline.name, Grade.grade)
        .select_from(Grade)
        .join(Discipline)
        .join(Student)
        .join(Group)
        .where(and_(Group.id == group_id, Discipline.id == discipline_id))
        .order_by(Student.name)
        .limit(10)
        .all()
    )
    return res


"""SELECT t.fullname AS teacher, d.name AS discipline, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g 
JOIN disciplines d ON d.id = g.discipline_id 
JOIN teachers t ON t.id = d.teacher_id 
WHERE t.id = 4
GROUP BY d.name 
ORDER BY d.name
LIMIT 5;"""


def select_8(teacher_id):
    res = (
        session.query(
            Teacher.name,
            Discipline.name,
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Discipline)
        .join(Teacher)
        .filter(Teacher.id == teacher_id)
        .group_by(Teacher.name, Discipline.name)
        .order_by(desc("avg_grade"))
        .all()
    )
    return res


"""SELECT s.fullname AS student, d.name AS discipline
FROM students s 
JOIN grades g ON g.student_id = s.id 
JOIN disciplines d ON d.id = g.discipline_id 
WHERE s.id = 1
GROUP BY d.name 
ORDER BY d.name
LIMIT 5;"""


def select_9(student_id):
    res = (
        session.query(Student.name, Discipline.name)
        .select_from(Grade)
        .join(Discipline)
        .join(Student)
        .filter(Student.id == student_id)
        .group_by(Student.name, Discipline.name)
        .all()
    )
    return res


"""SELECT d.name AS discipline, s.fullname AS student, t.fullname AS teacher
FROM students s 
JOIN grades g ON g.student_id = s.id 
JOIN disciplines d ON d.id = g.discipline_id 
JOIN teachers t ON d.teacher_id 
WHERE s.id = 1 AND t.id = 4
GROUP BY d.name 
ORDER BY d.name
LIMIT 5;"""


def select_10(student_id, teacher_id):
    res = (
        session.query(Discipline.name, Student.name, Teacher.name)
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Teacher)
        .filter(and_(Student.id == student_id, Teacher.id == teacher_id))
        .group_by(Teacher.name, Discipline.name, Student.name)
        .all()
    )
    return res


"""SELECT ROUND(AVG(g.grade)) AS average_grade, t.fullname AS teacher, s.fullname AS student
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN disciplines d ON d.id = g.discipline_id 
JOIN teachers t ON t.id = d.teacher_id 
WHERE t.id = 4 AND s.id = 1
LIMIT 5;"""


def select_11(
    teacher_id,
    student_id,
):
    res = (
        session.query(
            func.round(func.avg(Grade.grade), 1).label("avg_grade"),
            Teacher.name,
            Student.name,
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Teacher)
        .filter(and_(Student.id == student_id, Teacher.id == teacher_id))
        .group_by(Teacher.name, Student.name)
        .all()
    )
    return res


"""SELECT s.fullname AS student, g.grade, d.name AS discipline, g.date_of AS date
FROM grades g 
JOIN students s ON s.id = g.student_id 
JOIN groups g2 ON g2.id = s.group_id 
JOIN disciplines d ON d.id = g.discipline_id 
WHERE g2.id = 1 AND d.id = 4 AND g.date_of = (SELECT MAX(date_of) FROM grades WHERE discipline_id = d.id AND student_id = s.id)
LIMIT 5;"""


def select_12(group_id, discipline_id):
    res_subquery = (
        select(Grade.date_of_grade)
        .join(Student)
        .join(Group)
        .where(and_(Grade.discipline_id == discipline_id, Group.id == group_id))
        .order_by(desc(Grade.date_of_grade))
        .limit(1)
        .scalar_subquery()
    )

    res = (
        session.query(
            Student.name, Grade.grade, Discipline.name, Group.name, Grade.date_of_grade
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Group)
        .filter(
            and_(
                Discipline.id == discipline_id,
                Group.id == group_id,
                Grade.date_of_grade == res_subquery,
            )
        )
        .order_by(desc(Grade.date_of_grade))
        .all()
    )
    return res


def print_queries_res():
    print("SELECT_1:")
    result_1 = select_1()
    pprint(result_1)

    print("\nSELECT_2:")
    result_2 = select_2(3)
    pprint(result_2)

    print("\nSELECT_3:")
    result_3 = select_3(3)
    pprint(result_3)

    print("\nSELECT_4:")
    result_4 = select_4()
    pprint(result_4)

    print("\nSELECT_5:")
    result_5 = select_5(3)
    pprint(result_5)

    print("\nSELECT_6:")
    result_6 = select_6(3)
    pprint(result_6)

    print("\nSELECT_7:")
    result_7 = select_7(3, 3)
    pprint(result_7)

    print("\nSELECT_8:")
    result_8 = select_8(3)
    pprint(result_8)

    print("\nSELECT_9:")
    result_9 = select_9(3)
    pprint(result_9)

    print("\nSELECT_10:")
    result_10 = select_10(3, 3)
    pprint(result_10)

    print("\nSELECT_11:")
    result_11 = select_11(3, 3)
    pprint(result_11)

    print("\nSELECT_12:")
    result_12 = select_12(3, 3)
    pprint(result_12)


if __name__ == "__main__":
    print_queries_res()

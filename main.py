import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

with open('ddl.sql', 'r') as f:
    db_script = f.read()

cursor.executescript(db_script)


# -- Задание 1
# -- Вывести в таблице:
# --  * имя департамента
# --  * количество сотрудников с ЗП
# --  * количество сотрудников с грейдом "А"
# --  * количество сотрудников с другими грейдами
# --  * максимальную ЗП по департаменту
# --  1. + Отсортировать по (Имени департамента, размеру ЗП: двойнай сортировка)
# --  2. + Для департаментов, в которых 0 сотрудников.
# --
# -- Решение ниже на диалекте SQLite

def first_task():
    sql = """
    SELECT 
        department.name,
        COUNT(CASE WHEN salary.salary IS NOT NULL THEN 1 END) AS users_count,
        COUNT(CASE WHEN user.grade = 'A' THEN 1 END) AS users_grade_a_count,
        COUNT(CASE WHEN user.grade != 'A' THEN 1 END) AS users_grade_not_a_count,
        COALESCE(MAX(salary.salary), 0) AS max_salary
    FROM department 
        LEFT JOIN mtm ON (mtm.department_id = department.id)
        LEFT JOIN user ON (user.id = mtm.user_id)
        LEFT JOIN salary ON(salary.user_id = user.id)
    GROUP BY department.id
    ORDER BY department.name, max_salary
    """
    cursor.execute(sql)
    print(list(map(lambda x: x[0], cursor.description)))
    return cursor.fetchall()
    

# -- Задание 2
# -- Вывести в таблице
# --  * имя сотрудника
# --  * грейд сотрудника
# --  * зарплата сотрудника
# --  * количество департаментов, в которых числится сотрудник
# --
# --  1. Отсортировать по (Имени сотрудника, количеству департаментов по убыванию)

# --
# -- Решение ниже на диалекте SQLite
def second_task_by_name():
    sql = """
    SELECT 
        user.name,
        user.grade,
        salary.salary,
        COUNT(department.id) AS departments_count
    FROM user
        LEFT JOIN mtm ON (mtm.user_id = user.id)
        LEFT JOIN department ON (department.id = mtm.department_id)
        LEFT JOIN salary ON(salary.user_id = user.id)
    GROUP BY user.id
    ORDER BY user.name, departments_count DESC
    """
    cursor.execute(sql)
    print(list(map(lambda x: x[0], cursor.description)))
    return cursor.fetchall()

# --  2. + Сгруппировать по грейду, вывести:
# --   * Количество сотрудником с этим грейдом
# --   * Количество сотрудников c этим грейдом, которые числятся более чем в одном департаменте
# --   * среднюю ЗП сотрудников с этим грейдом
def second_task_by_grade():
    sql = """
    SELECT 
        u.grade AS grade_name,
        COUNT(u.id) AS count_with_grade,
        AVG(salary.salary),
        (
        SELECT 
            COUNT(user.id)
        FROM 
            user 
        LEFT JOIN mtm ON (mtm.user_id = user.id) 
        LEFT JOIN department ON (department.id = mtm.department_id)
        WHERE 
            user.grade=u.grade 
        GROUP BY user.id   
        HAVING(COUNT(department.id) > 1)
        ) AS has_many_departments
    FROM user AS u
        LEFT JOIN mtm ON (mtm.user_id = u.id)
        LEFT JOIN department ON (department.id = mtm.department_id)
        LEFT JOIN salary ON(salary.user_id = u.id)
    GROUP BY u.grade
    """
    cursor.execute(sql)
    print(list(map(lambda x: x[0], cursor.description)))
    return cursor.fetchall()


print("TASK 1")
print(first_task())
print("TASK 2 by name")
print(second_task_by_name())
print("TASK 2 by grade")
print(second_task_by_grade())
import pandas as pd
import random

departments = ['Отдел продаж', 'Отдел разработки', 'Отдел маркетинга', 'Отдел финансов']
male_names = ['Павел', 'Егор', 'Иван', 'Сергей', 'Олег', 'Алексей', 'Дмитрий', 'Артем', 'Александр', 'Максим', 'Кирилл', 'Никита']
female_names = ['Мария', 'Анна', 'Марина', 'Екатерина', 'София', 'Александра', 'Елена', 'Ольга', 'Полина', 'Юлия', 'Светлана', 'Анастасия']
male_surnames = ['Иванов', 'Петров', 'Сидоров', 'Ефремов', 'Николаев', 'Смирнов', 'Кузнецов', 'Морозов', 'Егоров']
female_surnames = ['Иванова', 'Петрова', 'Сидорова', 'Ефремова', 'Николаева', 'Смирнова', 'Егорова', 'Кузнецова', 'Морозова']
positions = ['Менеджер', 'Разработчик', 'Маркетолог', 'Финансовый аналитик']

employees = list()
names_surnames_used = set()

while len(employees) < 35:
    gender = random.randint(0, 1)
    if gender:
        name = random.choice(male_names)
        surname = random.choice(male_surnames)
    else:
        name = random.choice(female_names)
        surname = random.choice(female_surnames)

    department = random.choice(departments)
    position = random.choice(positions)
    salary = random.randint(100_000, 500_000)

    if (name, surname) in names_surnames_used:
        continue
    else:
        names_surnames_used.add((name, surname))
        employees.append([name, surname, department, position, salary])

df = pd.DataFrame(employees, columns=['Имя', 'Фамилия', 'Отдел', 'Должность', 'Зарплата'])

min_salary = df["Зарплата"].min()
max_salary = df["Зарплата"].max()

print(df)
print(f"Min salary: {min_salary}")
print(f"Max salary: {max_salary}")



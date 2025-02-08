class Student:
    def __init__(self, name: str, age: int, grade: str, scores: list):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def average_score(self):
        avg = sum(self.scores) / len(self.scores)
        return avg

student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])

print("Имя:", student2.name)
print("Возраст:", student2.age)
print("Класс:", student2.grade)
print("Оценки:", *student2.scores)
print("Средний балл:", student2.average_score())
class Student:
    """Класс, представляющий школьника.

    Этот класс позволяет хранить информацию о школьнике, включая его имя, возраст,
    класс и оценки. Также предоставляет метод для вычисления среднего балла.

    Attributes:
        name (str): Имя школьника
        age (int): Возраст школьника
        grade (str): Класс, в котором учится школьник
        scores (list): Список оценок школьника
    """

    def __init__(self, name: str, age: int, grade: str, scores: list):
        """Инициализирует экземляр класса Student

        Args:
            name (str): Имя школьника
            age (int): Возраст школьника
            grade (str): Класс, в котором учится школьник
            scores (list): Оценки школьника

        Raises:
            ValueError: Невалидное значение.
        """

        if not(isinstance(name, str) and isinstance(age, int) and isinstance(grade, str) 
            and isinstance(scores, list)):
            raise ValueError("Вы ввели невалидные значения")

        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def average_score(self):
        """Возвращает средний балл школьника

        Returns:
            avg (float): Средний балл школьника
        """
        avg = sum(self.scores) / len(self.scores)
        return avg


#Проверяем работу программы
student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])

print("Имя:", student2.name)
print("Возраст:", student2.age)
print("Класс:", student2.grade)
print("Оценки:", *student2.scores)
print("Средний балл:", student2.average_score())
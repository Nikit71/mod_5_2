#   Домашняя работа по уроку "Специальные методы классов"
#   Задача "Магические здания":

class House:
    def __init__(self, name, number_of_floors):
        self.name = (name)  #   имя
        self.number_of_floors =number_of_floors   #     кол - во этажей

    def __str__(self):
        self.str="Название: " + self.name + " кол-во этажей: " + str(self.number_of_floors)
        return self.str
    def __len__(self):
        return self.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
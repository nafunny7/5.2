class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors and new_floor >= 1:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return str(f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")






h1 = House("ЖК Солнечная Долина", 18)
h2 = House("ЖК Лебедь", 3)
h3 = House("ЖК Семерка", 7)
h3.go_to(7)
h2.go_to(52)
h1.go_to(13)
print(len(h1))
print(h1)
print(len(h2))
print(h2)
print(len(h3))
print(h3)

class APPLE:
    def __init__(self, variety, color, weight, diameter):
        self.variety = variety 
        self.color = color 
        self.weight = weight 
        self.diameter = diameter 

    def change_color(self, new_color):
        self.color = new_color

    def show_info(self):
        print(f"Сорт: {self.variety}, Колір: {self.color}, Маса: {self.weight}г, Діаметр: {self.diameter} см")

apples = [
    APPLE("Golden", "Жовтий", 150, 7),
    APPLE("Granny Smith", "Зелений", 160, 6),
    APPLE("Fuji", "Червоний", 170, 7)
]

apples[0].change_color("Зелений")

for apple in apples:
    apple.show_info()

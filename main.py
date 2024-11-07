import vector
import random

def generate_random_coordinates():
    return random.randint(-10, 10), random.randint(-10, 10)

x1, y1 = generate_random_coordinates()
x2, y2 = generate_random_coordinates()
vector1 = vector.VECTOR("Vector1", x1, y1, x2, y2)

x1, y1 = generate_random_coordinates()
x2, y2 = generate_random_coordinates()
vector2 = vector.VECTOR("Vector2", x1, y1, x2, y2)

vector1.ShowName()
print("Довжина:", vector1.GetLen())

vector2.ShowName()
print("Довжина:", vector2.GetLen())

result_vector = vector1.Plus(vector2)
result_vector.ShowName()
print("Довжина результатуючого вектора:", result_vector.GetLen())

if result_vector.is_in_third_quadrant():
    print(f"Вектор {result_vector.name} знаходиться в III чверті координатної площини")
else:
    print(f"Вектор {result_vector.name} не знаходиться в III чверті координатної площини")

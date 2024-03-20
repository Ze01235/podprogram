import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume


radius1 = 5
volume1 = calculate_sphere_volume(radius1)
print(f"Объем сферы с радиусом {radius1} равен {volume1}")

radius2 = 7
volume2 = calculate_sphere_volume(radius2)
print(f"Объем сферы с радиусом {radius2} равен {volume2}")
import math

def calculate_volume_of_sphere():
    radius1 = 30
    radius2 = 40
    volume1 = (4/3) * math.pi * (radius1 ** 3)
    volume2 = (4/3) * math.pi * (radius2 ** 3)
    return volume1, volume2

volume1, volume2 = calculate_volume_of_sphere()

print("Volume of the first sphere is", volume1, "and the second sphere is", volume2)

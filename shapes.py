import math

# Function to create an circle's area
def get_area_circle(radius):
    return math.pi * (radius**2)

def get_circumference(radius):
    return 2 * math.pi * radius

def get_area_square(side):
    return side * side

def get_area_of_triangle(base = 1, height = 1):
    return (base * height) / 2

print(get_area_circle(10))
print(get_circumference(10))
print(get_area_square(10))

get_area_of_triangle(height=15, base=10)
print(get_area_of_triangle(height=15, base=10))


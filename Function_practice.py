# 21. Calculate area of a triangle
# Input: base = 10, height = 6
# Output: Area = ?

def area_tringle():
    base = 10
    height = 6
    area = 0.5*base*height
    return area
res = area_tringle()
print(res)

# 22.Calculate perimeter of a square
# Input: side = 9
# Output: Perimeter = ?

def perimeter_of_square():
    side = 9
    perimeter = 4*side
    return perimeter
res = perimeter_of_square()
print(res)

# 23.Calculate diameter of a circle
# Input: radius = 14
# Output: Diameter = ?

def diameter_of_circle():
    radius = 14
    diameter = 2*radius
    return diameter
res = diameter_of_circle()
print(res)

# 24.Calculate volume of a cube
# Input: side = 5
# Output: Volume = ?

def volume_of_cube():
    side = 5
    volume = side**3
    return volume
res = volume_of_cube()
print(res)

# 25.Calculate surface area of a cuboid
# Input: l = 4, b = 3, h = 2
# Output: Surface Area = ?

def surfaceArea_of_cuboid():
    lenght = 4
    breadth = 3
    height = 2
    surface_area = lenght*breadth*height
    return surface_area
res = surfaceArea_of_cuboid()
print(res,"sqr.mtr")

# 26.Square of sum: (x + y)²
# Input: x = 5, y = 7
# Output: ?

def square_of_sum():
    x = 5
    y = 7
    expresion = (x+y)**2
    return expresion
res = square_of_sum()
print(res)

# 27.Simplify expression: x² - 4x + 4
# Input: x = 3
# Output: ?

def simplify_exp():
    x = 3
    exp = x**2 - 4*x + 4
    return exp
res = simplify_exp()
print(res)

# 25.Evaluate: (a + b)(a - b)
# Input: a = 6, b = 2
# Output: ?

def evaluate():
    a = 6
    b = 2
    Result = (a+b)*(a-b)
    return Result

res = evaluate()
print(res)

# 29.Sum of cubes: a³ + b³
# Input: a = 1, b = 2
# Output: ?

def sum_of_cubes():
    a = 1
    b = 2
    claculate = a**3 + b**3
    return claculate
res = sum_of_cubes()
print(res)

# 30.Simplify: (x - y)²
# Input: x = 10, y = 6
# Output: ?

def simplify():
    x = 10
    y = 6
    calculate = (x - y)**2
    return calculate
res = simplify()
print(res)

# 31.Difference of cubes: x³ - y³
# Input: x = 4, y = 1
# Output: ?

def difference_of_cubes():
    x = 4
    y = 1
    claculate = x**3 - y**3
    return claculate
res = difference_of_cubes()
print(res)
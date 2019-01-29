# Solucion primera parte


#Compute how many times, on average, do you have to throw a die (with only six faces) in order to reach reach a minimum of 100 points. In this game you start with 0 points, you throw the die and add the number you get to the total account. Use the results of random.random() to implement the die throw.

n_games = 10000
n_try = []
for i in range(n_games):
    n = 0
    points = 0
    while(points < 100):
        i = (random.random()*6)//1 + 1
        points += i
        n += 1
    n_try.append(n)
    

suma = 0
for i in range(n_games):
    suma += n_try[i]

promedio = suma/len(n_try)
print(promedio)


# Define a function distance that takes as arguments two lists a,b and computes the Euclidean distance between the two:

def distance(a,b):
    n = len(a)
    d = 0.0
    for i in range(n):
        d += (a[i] -b[i])**2
    d = math.sqrt(d)
    return d

print(distance([0,0], [1,1]))
print(distance([1,5], [2,2]))
print(distance([0,1,2], [2,3,4]))

# Redefine the class Circle to include a new method called perimeter that returns the value of the circle's perimeter.

class Circle:
    def __init__(self, radius):
        self.radius = radius #all attributes must be preceded by "self."
    def area(self):
        import math
        return math.pi * self.radius * self.radius
    def perimeter(self):
        import math
        return 2.0  * math.pi * self.radius


#Define the class Vector3D to represent vectors in 3D. The class must have

#Three attributes: x, y, and z, to store the coordinates.

#A method called dot that computes the dot product

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def dot(self, v):
        return self.x  * v.x + self.y * v.y + self.z * v.z

v = Vector3D(2, 0, 1)
w = Vector3D(1, -1, 3)
print(v.dot(w))

# Import the module random and use the function shuffle to shuffle the contents of a list that has the integers from 0 to 9. Print the list before and after shuffling. Use random.shuffle? to read the documentation string for that function. 

import random

a = list(range(10))
print(a)
random.shuffle(a)
print(a)

# Solucion segunda parte

class Contador:
    def __init__(self, archivo):
        self.archivo = archivo
    def cuenta_lineas(self):
        f = open(self.archivo)
        lineas = f.readlines()
        return len(lineas)
    def cuenta_caracteres(self, letra):
        f = open(self.archivo)
        lineas = f.readlines()
        c = 0
        for linea in lineas:
            for item in linea:
                if item==letra:
                    c += 1
        return c


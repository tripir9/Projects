# Fibonacci Sequence
# Enter a number and have the program generate 
# the Fibonacci sequence to that number or to the Nth number.

long = input("Introduzca numeros")
a = 1
b = 0
c = 0

for i in range(long):
    print a
    b = a
    c = b
    a = b + c

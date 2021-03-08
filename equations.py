from math import *

# First One (a + b)² :
 
a = int(input("a = ? :"))
b = int(input("b = ? :"))

solution = pow(a,2) + (2*a*b) + pow(b,2)
print(f"The solution is {solution}")

# Second One (a + b)³ :

a = int(input("a = ? :"))
b = int(input("b = ? :"))

solution = pow(a,3) + pow(b,3) + (3*(pow(a,2))*b) + (3*(pow(b,2))*a)
print(f"The solution is {solution}")

# Third One ( a² - b² ) :

a = int(input("a = ? :"))
b = int(input("b = ? :"))

solution =  (a-b) * (a+b)
print(f"the solution is {solution}")


# Fourth One ( ax² + bx + c = 0 ) :

a = int(input("a = ? :"))
b = int(input("b = ? :"))    
c = int(input("c = ? :"))

Delta = pow(b,2) - (4 * a *c)
print(f"Delta = {Delta}")

if Delta == 0 :
    solution = -b/(2*a)
    print(f"When Delta = 0 \n Then the solution will be {solution}")
elif Delta > 0 :
    solution1 = (-b - sqrt(Delta)) / (2*a)
    solution2 = (-b + sqrt(Delta)) / (2*a)
    print(f"When Delta > 0 \n Then we have two solutions : {solution1} , {solution2} ")
else :
    print("When Delta < 0 \n Sorry the solution is not available right now :)")


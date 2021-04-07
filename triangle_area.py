import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a+b+c)/2
area1 = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(" Area of the triangle is: ", area1)

area = 0.25 * math.sqrt((a+b+c)*(b+c-a)*(a-b+c)*(a+b-c))
print(" Area of the triangle is: ", area)
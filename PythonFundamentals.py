import requests
print(requests.__version__)

#Print
print("Hello World")
print("I am learning python for kp1")

#How to check a variable's data type
name = "hasan"
age = 27
height = 5.9
Is_student = False
print(type(name))
print(type(age))
print(type(height))
print(type(Is_student))

#Type Casting
a = 10
b = 5.5
result = a + b
print(result)
print(type(result))
#2
age = "25"
age = int(age)
print(age)
print(type(age))
#3
x = "100"
y = 20
print(int(x) + y)

#Python operators
print(f"Division:{10/3},FloorDivision:{10//3},Modulus:{10%3},Add:{10+3},Sub:{10-3},Multiple:{10*3},Exponentiation:{10**3},")

#Increment and decrement operators
x = 10
x /= 5
print(x)

#Comparison operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a < b)
print(a > b)

#Logical operators
age = 16
has_id = True
print(age > 18 and has_id) #False
print(age > 18 or has_id)  #True

#list
languages = ["Python", "Java", "JavaScript"]
print(languages)
print(languages[0])
print(languages[1])
print(languages[2])





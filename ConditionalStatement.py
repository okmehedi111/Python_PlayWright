#Conditional Statement
age = 16
if age >= 18:
    print("You are adult")
else:
    print("You are teenager")

marks = 75
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

#Nested if else
username = "admin"
password = "12345"

if username == "admin":
    if password == "12345":
        print("Login Successful")
    else:
        print("Password is incorrect")
else:
    print("incorrect username")

#Ternary operator
age = 16
if age >= 18:
    result = "Adult"
else:
    result = "Teenager"
print(result)

age = 16
result = "Adult" if age >= 18 else "Teenager"
print(result)





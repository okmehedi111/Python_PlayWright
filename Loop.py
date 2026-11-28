#for loop
for i in range(1,11,3) :
    print(i)

test_cases = ["tc01", "tc02", "tc03"]
for test in test_cases :
    print(f"executing test case: {test}")

#While Loop
i = 1
while i <= 6:
    print(i)
    i += 1
for i in range(1,10,1) :
    if i == 3:
        break
    print(i)
for i in range(1,10,3) :
    for j in range(1,10,2) :
        print(f"i = {i} and j = {j}")

#task-1
age = 20
if age >= 18 :
    print("can vote")
else:
    print("can not vote")

#task-2
marks = 75
if marks >= 80 :
    print("Grade A")
elif marks >= 60 :
    print("Grade B")
elif marks >= 40 :
    print("Grade C")
else:
    print("Fail")

#task-3
number = 15
result = "even" if number % 2 == 0 else "odd"
print(result)

#task-4
languages = ["Python", "Java", "C++", "C", "C#"]
for language in languages :
    print(language)

#task-5
i = 1
while i <= 10:
    print(i)
    i += 1

#task-6
for i in range(1,11) :
    if i == 5:
        continue
    print(i)
for i in range(1,11) :
    if i == 8:
        break
    print(i)
for i in range(3) :
    print(i)
#lambda (lambda arguments: expression)
Multifly = lambda a,b: a*b
print(Multifly(10,20))
is_even = lambda x: x % 2 == 0
print(f"IS Even= {is_even(5)}") #Check whether a number is even
biger_number = lambda x,y: x if x > y else y
print(f"Bigger number= {biger_number(10,20)}")  #Find the bigger number

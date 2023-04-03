def add(P, Q):    
   return P + Q   
def subtract(P, Q):   
   return P - Q   
def multiply(P, Q):   
   return P * Q   
def divide(P, Q):   
   return P / Q    
    
print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
    
choice = input("Choice : ")    
    
a = int (input ("Enter the first number: "))    
b = int (input ("Enter the second number: "))    
    
if choice == 'a':    
   print (a, " + ", b, " = ", add(a, b))    
elif choice == 'b':    
   print (a, " - ", b, " = ", subtract(a, b))    
elif choice == 'c':    
   print (a, " * ", b, " = ", multiply(a, b))    
elif choice == 'd':    
   print (a, " / ", b, " = ", divide(a, b))    
else:    
   print ("Invalid input")  
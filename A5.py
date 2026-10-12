#SMALLEST AND LARGEST RESISTOR
r1=int(input("Enter your 1st Resistor : "))
r2=int(input("Enter your 2nd Resistor : "))
r3=int(input("Enter your 3rd Resistor : "))
 #LARGEST
if r1>=r2 and r1>=r3:
    largest=r1
elif r2>=r1 and r2>=r3:
        largest=r2
else:
        largest=r3

  #SMALLEST
if r1<=r2 and r1<=r3:
    smallest=r1
elif r2<=r1 and r2<=r3:
     smallest=r2
else:
     smallest=r3

print(f"Your largest Resistor is {largest}(ohm)")
print(f"Your smallest Resistor is {smallest}(ohm)")


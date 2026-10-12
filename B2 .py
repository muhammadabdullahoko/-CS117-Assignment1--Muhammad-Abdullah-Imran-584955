#RESISTORS IN SERIES
resistor=int(input("Enter the number of resistors in series :"))

total=0

for i in range(1,resistor+1):
    r=int(input(f"Enter R{i} :"))
    total+=r

print(f"Total resistance is : {total}")

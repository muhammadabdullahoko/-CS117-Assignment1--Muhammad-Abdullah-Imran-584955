#RESISTOR TOLERANCE SORTING
t1=0
t2=0
reject=0
value=float(input("Enter the value of resistor (0 to stop) :"))

while value!=0:
    if 99.0<=value<=101.0:
        t1+=1
        print(f"{value} falls in 1% tolerance")
    elif 95.0<=value<=105.0:
        t2+=1
        print(f"{value} falls in 5% tolerance")
    else:
        reject+=1
        print(f"{value} rejected")

    value=float(input("Enter the value of resistance (0 to stop) :"))

print(f"1% tolerance : {t1}")
print(f"5% tolerance : {t2}")
print(f"Reject : {reject}")

#PARALLEL RESISTANC
def parallel_resistance(resistors):
    total=0
    for r in resistors:
        total=total+1/r
    return 1/total

value=input("Enter resistors by space")
resistors=[float(x) for x in value.split()]
print(parallel_resistance(resistors))

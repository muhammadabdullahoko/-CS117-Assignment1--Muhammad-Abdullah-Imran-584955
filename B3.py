#SENSOPR READING
reading=(3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
count=0
total=0
highest=reading[0]
lowest=reading[0]
for v in reading:
    if v > 3.2:
        count+=1
    if v > highest:
        highest=v
    if v < lowest:
        lowest=v
    total+=v
average=total/7

print(f"(a) Number of readings above '3.2'V : {count}")
print(f"(b) Highest reading : {highest}V")
print(f"(c) Lowest reading : {lowest}V")
print(f"Average of reading : {average}")

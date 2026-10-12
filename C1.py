#CURRENT AND POWER
def ohms_current(v,r):
    return v/r

def power_dissipation(i,r):
    return i**2 *r

v=12
r=6

i=ohms_current(v,r)
p=power_dissipation(i,r)

print(f"Current = {i} A")
print(f"Power dissipation = {p} W")

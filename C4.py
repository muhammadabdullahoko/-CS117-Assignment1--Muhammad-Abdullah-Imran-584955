#LOADED VOLTAGE DIVIDER
def loaded_divider(vs,r1,r2,rl):
    unloaded=vs*r2/(r1+r2)
    r_parallel=(r2*rl)/(r2+rl)
    loaded=vs*r_parallel/(r1+r_parallel)
    return round(unloaded,2),round(loaded,2)
vs=float(input("Enter source voltage (vs) : "))
r1=float(input("Enter r1 : "))
r2=float(input("Enter r2 : "))
rl=float(input("Enter load resistor (rl) : "))
print(loaded_divider(vs,r1,r2,rl))

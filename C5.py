#STAR-DELTA TRANFORMATION
def star_to_delta(ra,rb,rc):
    r_nume=(ra*rb)+(rb*rc)+(ra*rc)
    rab=r_nume/rc
    rbc=r_nume/ra
    rac=r_nume/rb
    return round(rab,2),round(rbc,2),round(rac,2)
ra=float(input("Enter Ra :"))
rb=float(input("Enter Rb :"))
rc=float(input("Enter Rc : "))

print("Delta values(Rab,Rbc,Rac) : ",star_to_delta(ra,rb,rc))

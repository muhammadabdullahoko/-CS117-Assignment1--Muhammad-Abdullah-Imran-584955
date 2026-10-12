#FUSE CHECK
voltage=float(input("Enter voltage(V):"))
resistance=float(input("Enter resistance(ohm):"))
if resistance <=0:
   print("Invalid resistance")
else:
     current=voltage/resistance
     print(f"Your current is: {current}")
     if current >=2:
        print("Fuse will Blow")
     else:
          print("Circuit is safe")

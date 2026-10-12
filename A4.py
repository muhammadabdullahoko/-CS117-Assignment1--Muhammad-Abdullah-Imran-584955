#LOGIC GATES
a=int(input("Enter a : "))
b=int(input("Enter b : "))
      
if a not in (0,1) or b not in (0,1):
      print("Bits must be 0 or 1")
else:
    AND= a and b              #For AND can write just "and"
    OR= a or b                #For OR can write just "or"
    XOR= a ^ b                #For XOR need to write "^"
    print(f"AND is : {AND}")
    print(f"OR is : {OR}")
    print(f"XOR is : {XOR}")

#DECIMAL TO BINARY
def decimal_to_binary(n):
    whole=int(n)
    fraction=n-whole
    binary=""
    while whole>0:
        binary=str(whole%2)+binary
        whole=whole//2
     if binary=="":         
        binary="0" 
    binary+="."
    for i in range(8):
        fraction*=2
        binary+=str(int(fraction))
        fraction-=int(fraction)
    return binary

num=float(input("Enter a positive decimal you want to convert to binary : "))
print(decimal_to_binary(num))

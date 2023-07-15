def binarytodecimal(binary):
    decimal, i=0,0
    while(binary!=0):
        dec=binary%10
        decimal=decimal+dec*pow(2,i)
        binary=binary/10
        i+=1
    print(decimal)
binarytodecimal(10111001)
def OctToHex(n):
    print("Octal", n)
    decimal=int(n, 8)
    hexadecimal=hex(decimal).replace("0x")
    print("equal value=", hexadecimal)
OctToHex("752")
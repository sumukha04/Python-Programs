val=int(input("enter the number: "))
str_val=str(val)
if str_val==str_val[::-1]:
    print("Palindrome")
    for i in range (10):
        if str_val.count(str(i))>0:
            print(str(i), "Appears", str_val.count(str(i)), "times")
str1=input("enter the string")
str2=input("enter the string")
if len(str2)<len(str1):
    short=len(str2)
    long=len(str1)
else:
    short=len(str1)
    long=len(str2)
    matchent=0
    for i in range(short):
        if str1[i]==str2[i]:
            matchent+=1
        print("Similarity between two said strings")
        print(matchent/long)
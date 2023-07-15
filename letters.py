s=input("Enter a sentence: ")
w=v=d=l=0
l_w=s.split()
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isupper():
        v=v+1
    elif c.islower():
        l=l+1
print("number of words", w)
print("number of digits", d)
print("number of uppercase", v)
print("number of lowercase", l)
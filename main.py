n = int(input("enter a number"))
a= 0
t= n
while t!=0:
    digit= t % 10
    a= a + digit**3
    t= t//10
print(a)
if n== a:
    print("its an armstrong number")
else:
    print("its not a armstrong number")    
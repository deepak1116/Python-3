chk = []
primenum = []
nonprime = []
num = int (input("Enter end of range to know the prime number in between : "))
def prime(a):
    for  i in range(2,a):
        if((a==1) or(a==2)):
           chk.append(1)
        else:
           chk.append(a%i)
    if 0 in chk:
        nonprime.append(a)
    else:
        primenum.append(a)
for i in range(1,num):
    prime(i)
    chk = []
print("prime numbers : ",primenum)
#print("non prime numbers : ",nonprime)

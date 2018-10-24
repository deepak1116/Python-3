while True:
    a= int(input("Enter the  number: "))
    count= 1
    for i in range(2,a):
       if((a%i) > 0 ):
          count += 1
       else:
          count -= 1
    if(count>0):
       print("prime")
    else:
       print("non prime")

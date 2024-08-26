n=int(input("Enter a No:"))
i=2
f=0
while(i<n/2):
    if(n%i==0):
        f=1
        break
    i+=1
if(f==1):
    print("Not a prime no:")
else:
    print(n,"prime no")

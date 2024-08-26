a = int(input("Enter a number: "))
temp = a
sum1 = 0
while temp > 0:
    d = temp % 10
    sum1 += d**3
    temp //= 10
if sum1 == a:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

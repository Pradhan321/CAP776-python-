sq=[num*num for num in range(1,11)]
print(sq)



for n in range(2,11):
    for m in range(1,11):
      print("%-3d"%(n*m),end=' ')
    print()

a=input("Enter a number")
b=input("enter a second number")
sorted_a=''.join(sorted(a))
sorted_b=''.join(sorted(b))

if(sorted_a==sorted_b):
    print("number is anagram")
else:
        print("number is not a anagram")

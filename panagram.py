a=input("Enter a sentence")
a=a.lower()
b="abcdefghijklmnopqrstuvwxyz"
is_panagram=True
for letter in b:
 if(letter not in a):
  is_panagram=False 
 break
if is_panagram:
 print("The sentence is a panagram")
else:
    print("the sentence is not a panagram")

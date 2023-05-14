x= input("enter the character:")
if (x>='a' or x<='z'):
    print("it is lower case")
elif (x>='A' or x<='Z'):
    print("it is uper case")
elif (x>=1 or x<=9):
    print("it is numeric")
else:
    print("it is a special character")
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select")
print("1-ADD")
print("2-SUBTRACT")
print("3-MULTIPLICATION")
print("4-DIVISION")

choice=input("Enter choice(1,2,3,4):")
x=float(input("enter 1st number:"))
y=float(input("enter 2nd number:"))

if choice == '1':
    print(f"The result is: {add(x, y)}")
elif choice == '2':
    print(f"The result is: {sub(x, y)}")
elif choice == '3':
    print(f"The result is: {mul(x, y)}")
elif choice == '4':
    print(f"The result is: {div(x, y)}")
else:
    print("Invalid input")





def ii( which ):
    print("Enter",which,"integer: ", end="")
    return int(input())


a = ii("first")
b = ii("second")


op = input("Choose operation (* / - + **): ")

res = 0

if op == "+":
    res = a + b
elif op == "*":
    res = a * b
elif op == "/":
    res = a / b
elif op == "-":
    res = a - b    
elif op == "**":
    res = a ** b

else :
    print("Wrong operation")

print("Result: ", res)


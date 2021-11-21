a =int(input("Enter first number: "))
e = int(input("Enter second number: "))
i = int(input("Enter third number: "))

def greatest(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3


s = greatest(a, e, i)
print("Greatest of all three input numbers is " + str(s))
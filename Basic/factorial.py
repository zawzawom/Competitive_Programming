fact = int(input("Enter a Number"))
factorial = 1
i = 1
for i in range(1,fact+1):
    factorial = factorial*i
    print(factorial)
print("Factorial of ",fact,"is ",factorial)
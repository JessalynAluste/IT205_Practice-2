num1 = int (input("Enter the first number: "))
int(num1)
num2 = int (input("Enter the second number: "))
int(num2)
num3 = int (input("Enter the limit: "))

multiples =[f for f  in range(num3) if f % num1 == 0 or f % num2 == 0]

sum = sum(multiples)


print(f"The sum of multiples of {num1} or {num2} up to {num3} is: {sum}")



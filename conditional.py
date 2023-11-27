num1=input('Give me the first number: ')
num2=input('Give me the second number: ')
num3=input('Give me the third number: ')

# Finding the largest number between three numbers
if(num1>num2):
    if(num1>num3):
        print('The big Number is ',num1)
    else:
        print('The big Number is ',num3)
else:
    if(num2>num3):
        print('The big Number is ',num2)
    else:
        print('The big Number is ',num3)


if(num1>num2 and num1>num3):
    print(f'The Largest Number is: {num1}')
elif(num2>num1 and num2>num3):
    print(f'The Largest Number is: {num2}')
else:
    print(f'The Largest Number is: {num3}')
# string concatenation

string = input('Please inter your quote: ')
print("Your quote is :", string)


# temperature calculator

# fahrenheit = float(input('Please enter the fahrenheit temperature :'))

# celsius = (fahrenheit - 32) / 1.8

# print('% 0.1f degree fahrenheit is = %0.1f degree celsius '%(fahrenheit,celsius))


# radius calculator

# import math

# radius = float(input('Please input the radius of a circle :'))
# area = math.pi * radius * radius
# print('Aria of the circle is = %0.5f'%(area))


# Number checker

# Number = int(input('Please input the Number : '))

# if(Number % 2 == 0):
#     print('The number your entered is an even number')
# else:
#     print('The number your entered is an odd number')


# change the value of tow number

# x = input('Enter the value of X : ')
# y = input('Enter the value of Y : ')

# temp = x
# x = y
# y = temp

# print('After swaping the X  value is:', x, 'and the Y  value is :',y )


# positive and negative number checker

# num = float(input('Enter the number : '))

# if num < 0:
#     print("The number is a negative number")
# elif num == 0:
#     print('The number is zero!')
# else:
#     print('The number is a positive')


# find the bigest number of three number

# number1 = float(input('Input first number : '))
# number2 = float(input('Input second number : '))
# number3 = float(input('Input third number : '))

# if (number2<number1) and (number3<number1):
#     largest = number1
# elif (number1<number2) and (number3<number2):
#     largest = number2
# else:
#     largest = number3

# print('The largest number is :',largest)


# deghat formula

# import math

# a = int(input('Enter the value of a: '))
# b = int(input('Enter the value of b: '))
# c = int(input('Enter the value of c: '))

# d = (b*b) - (4*a*c)

# if d==0 :
#     x = -b/(2*a)
#     print('Roots are real and equal and : ',x,x)
# elif (d>0):
#     x1 = (-b+math.sqrt(d)/(2*a))
#     x2 = (-b-math.sqrt(d)/(2*a))
#     print('Root are real and uniq and are :',x1,x2)
# else :
#     print('Root are imaginary')

# leap year checker

# year = int(input("Please Enter the value of year : "))

# if (year % 4 == 0 and year != 0 or year % 400 == 0):
#     print("This is a leap Year!")
# else:
#     print("This year is not leap year yet!")


# prime number checker

# num = int(input('Enter a number: '))

# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print(num," is not a prime number!")
#             break
#         else:
#             print(num," is a prime number!")
#             break
# else:
#     print(num," is a prime number!")


# factorial

# num = int(input('Enter a number: '))
# factorial = 1

# if num <0:
#     print("Sorry factorial does not exist for the negative number!")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial = factorial*i
# print("The factorial of ",num,' is ',factorial)


# fibonacci

# terms = int(input('How many terms: '))
# n1 = 0
# n2 = 1
# count = 0

# if terms<0:
#     print("Please inter a positive number!")
# elif terms == 1:
#     print('Fibonacci sequence up to ',terms," : ",n1)
# else:
#     print("Fibonacci sequence up to ",terms,' : ')
#     while count < terms:
#         print(n1,end=' , ')
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1

# find even number from 1 to 10

# for i in range(1,10+1):
#     if i % 2==0:
#         print(i)


# find the prime number from 1  to 10

# lower = int(input("Input the lower number: "))
# upper = int(input('Input the upper number: '))

# print('Prime number between',lower ,' and ',upper, ' is :')

# for num in range(lower,upper+1):
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0 :
#                 break
#         else:
#             print(num)


# recursive fibonacci sequence

# def recursive_fibonacci(n):
#     if n <= 1:
#         return 1
#     else:
#         return (recursive_fibonacci(n - 1)+recursive_fibonacci(n-2))
# terms= int(input("How many terms: "))
# if terms <=0:
#     print(
#         'Please input a positive number!'
#     )
# else:
#     print("Fibonacci sequence is :")
#     for i in range(terms):
#         print(recursive_fibonacci(i))

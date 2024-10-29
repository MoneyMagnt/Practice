#Simple Calculator

# num1 = float(input("Input a number: "))
# op = input("operator: ")
#num2 = float(input("Input another number"))

# if op == "+":
#     print(num1 + num2) 
# elif op == "-":
#     print(num1 - num2)    
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("INVALID OPERATOR")   


#Temperature Converter
# import math
# print("1.Degree to Fahrenheit")
# print("2.Fahrenheit to Degree")
# Cvt = input("Select your converter: ")
# if Cvt == "1":
#     Deg = float(input("temperature in Degree Celsuis: "))
#     print(f'{(Deg*9/5)+32} fahrenheit')
# elif Cvt == "2":
#     Fah = float(input("temperature in fahrenheit: "))
#     print(f'{(Fah - 32)*5/9} Degree Celsuis')
# else :
#     print("INVALID ENTRY!")    

#Mad lips
# color = input("What's your favorite color: ")
# name = input("What's your name: ")
# Favorite = input("Celebrity Crush: ")
# print(f'Roses are {color}')
# print('My name is {name}')
# print(f'my celebrity crush is {Favorite}')

#Tip Calculator
# tamount = float(input("What's the total amount: "))
# tpnt =float(input("percentage of tip: "))

# print((tpnt/100)*tamount)

#Grade Calculator
# score = int(input("Input score: "))
# if score >= 80 and score <= 100:
#     print("A1")
# elif score >= 75 and score <= 79: 
#     print("B+")  
# elif score >= 70 and score <= 74:
#     print("B-")
# elif score >= 60 and score <= 69:
#     print("B")
# elif score >= 50 and score <= 59: 
#     print("C+")
# elif score >= 0  and score <= 49:
#     print("F9")
# else:
#     print("INVALID SCORE!!")

#Leap Year Checker
# print ("Welcome to leap checker. ")
# year = int(input("Input Year: "))
# if year%4 == 0:
#     print("This is a leap.")
# else:
#     print("This is not a leap year, try again")    

secret_word = "MoneyMagnet"
guess = ""
guess_count = 3
out_of_guess = False
guess == secret_word and not(out_of_guess):
if guess_count < out_of_guess:
     guess = input("What's the secret word: ")
     guess_count =+ 1

if out_of_guess:
    print("Out of guess, you lose! ")
else:    
    print("You win!")
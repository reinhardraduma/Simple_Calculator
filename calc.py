#calc program5
from timer_calc import timer
import ast


def add(*numbers):
    numbers = input("Kindly input numbers you want to add? ")
    number_without_space = numbers.replace(" ", ",")#we are replacing wherever there is a space with a comma
    numbers_as_list= number_without_space.split(",") #converts the string into a list
    summation = 0
    for number in numbers_as_list: #looping inside a string
        if number.isdigit(): #type(number) == int or float
            number = float(number)
            summation += number
        else:
            return print("Kindly enter numbers only!!")
    print(f"The answer is: {summation}")
    return summation 

def subtract(*numbers):
    numbers = input("Kindly input numbers you want to Subtract? ")
    number_without_space = numbers.replace(" ", ",")#we are replacing wherever there is a space with a comma
    numbers_as_list= number_without_space.split(",") #converts the string into a list
    try:
        num_list_float = [float(num) for num in numbers_as_list]#using list comprehension to convert whats in num_as_list to float
        total= num_list_float[0]

        for number in num_list_float[1:]: #looping inside a string
            total -= number
        print(f"The answer is: {total}")
        return total 

    except Exception as e:
        return print("Kindly enter numbers only!!", e)
    
def division(*numbers):
    numbers = input("Kindly input numbers you want to divide? ")
    number_without_space = numbers.replace(" ", ",")#we are replacing wherever there is a space in our input with a comma
    numbers_as_list= number_without_space.split(",") #converts the string into a list
    total  = numbers_as_list[0]#trying to access the first item in our list using indexing  to cover for cases only 1 number is provided
    try:
        if len(numbers_as_list) > 1:#we check if the number of items is more than 1 if so we enter the if statements
            for number in numbers_as_list[1:]: #looping inside a list ad from index 1 since index 0 is covered above ie using total
                if number.isdigit(): #
                    total= float(total)#converting total to a float to avoid type error that will arise in line 61 as we can multipl sequence with non in type
                    number = float(number)
                    total = total / number
                else:
                    return print("Kindly enter numbers only!!")
            print(f"The answer is: {total}")
            return total 
        else:
            print(total)
    except ZeroDivisionError:
        print("The denominator shouldn't be 0")

def multiply(*numbers):
    numbers = input("Kindly input numbers you want to multiply? ")
    number_without_space = numbers.replace(" ", ",")#we are replacing wherever there is a space in our input with a comma
    numbers_as_list= number_without_space.split(",") #converts the string into a list
    total  = numbers_as_list[0]#trying to access the first item in our list using indexing  to cover for cases only 1 number is provided
    if len(numbers_as_list) > 1:#we check if the number of items is more than 1 if so we enter the if statements
        for number in numbers_as_list[1:]: #looping inside a list ad from index 1 since index 0 is covered above ie using total
            if number.isdigit(): #
                total= float(total)#converting total to a float to avoid type error that will arise in line 61 as we can multipl sequence with non in type
                number = float(number)
                total = total * number
            else:
                return print("Kindly enter numbers only!!")
        print(f"The answer is: {total}")
        return total 
    else:
        print(total)

def evaluate_bodmas():
    expression = input("kindly input an expression: ")
    try:
        result = ast.literal_eval(expression)
        print(f" The result is : {result}")
        return result
    except Exception as e:
        print("Kindly enter the correct BODMAS expression")
        return None
    

#check more on how to add  names like add etc
@timer
def symbol_check():
    
    while True:
        print("=" * 100)
        print("WELCOME TO MY RAD'S CALCULATOR PROGRAM")
        print("To exit --> exit")
        input_operation = input("Kindly type in the mathematics operation: ")
        
        if input_operation.lower() == "exit":
            print("Exiting from my_calc... Goodbye")
            break
        elif input_operation in ('+', "add","addition"):# used in instead of  == as in libne 81 as it accepts multiple
            add()
        elif input_operation in ("-", "minus", "subtract"):
            subtract()
        elif input_operation in  ("*","multipy","product","multiplication"):
            multiply()
        elif input_operation in ("/", "division", "divide"):
            division()
        elif input_operation in ("expression", "Bodmas", "BODMAS", "bodmas"):
            evaluate_bodmas()
        else:
            print("Kindly enter numbers correct symbol!!")
            return
        print("=" * 100)#we use it for better readability and seperate different times the program execute


#print(add(5,6.3,9,6))   

def main():
    symbol_check() 

main()

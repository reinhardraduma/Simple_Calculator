from sympy import *
from timer_calc import timer
import re


@timer #created this so i can time the execution time when the operation is working
def single_math_expression(expression):
    allowed_locals = {"sin":sin, "sinh":sinh,"cos":cos, "cosh":cosh, "tan":tan,"tanh":tanh,"log":log,"ln":ln,"e":E,"sqrt":sqrt, "pi":pi }
    expression = re.sub(r"(\d+)\s*%\s*(\d+)", r"Mod(\1,\2)", expression)#used rgex to substitute 
    expression = re.sub(r"(\d+)\s*^\s*(\d+)", r"(\1**\2)", expression)
    result = float(sympify(expression,locals=allowed_locals))#converting to float helps to convert a mixed number to decimal and use local that scope thru dict

    print(f"The result is : {result:.4f}")#rounding the float to 4 digits
    print("="*100)


def evaluate_math_expressions():
    while True:
        expression = input("kindly input an expression: ").strip()#removes leading and trailing white spaces
        if expression.lower() in ("exit","quit","end","kill"):
            print("Shutting down...")
            break
        else:
            try:
                single_math_expression(expression)#calling the function 
            except Exception as e:
                print("Kindly enter the correct expression.",e)
                print("For expressions/functions containing sin, cos... do add () e.g sin(30)")
                

def main_func():
    print("WELCOME TO MY SIMPLE CALCULATOR PROGRAM")
    evaluate_math_expressions()
    

main_func()
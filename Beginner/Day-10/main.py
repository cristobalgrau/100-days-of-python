#Calculator
import art

#Add function
def add (n1, n2):
    return n1 + n2

#Subtract function
def subtract (n1, n2):
    return n1 - n2

#Multiply function
def multiply (n1, n2):
    return n1 * n2

#Divide function
def divide (n1, n2):
    return n1 / n2


operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

print (art.logo)
num1 = float(input("What's the first number?: "))
repeat = True
while repeat:
    for symbol in operations:
        print (symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    
    calculation_function = operations[operation_symbol]
    result = calculation_function(num1, num2)
    
    print (f"{num1} {operation_symbol} {num2} = {result}")
    
    if input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ").lower() == "y":
        num1 = result
    else:
        repeat = False
        print ("Goodbye!.")

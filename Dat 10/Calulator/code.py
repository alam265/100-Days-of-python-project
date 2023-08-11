from replit import clear 

def addition(n1,n2):
    return n1+n2 
def substraction(n1,n2):
    return n1-n2 
def multiplication(n1,n2):
    return n1*n2 
def divide(n1,n2):
    return n1/n2 

operations = {
    '+':addition ,
    '-':substraction,
    '*':multiplication,
    '/':divide
}

print("-----Welcome to my Calculator-------")

def calculator():
    n1 = float(input("Enter first number: "))
    for k in operations.keys():
        print(k)

    


    while True: 
        operator = input("Enter operator: ")
        n2 = float(input("Enter second Number: "))
        result = operations[operator](n1,n2)
        print(f"{n1} {operator} {n2} = {result} ")
        
        ip = input("Are you wanna do further calculation? type 'yes'  or type 'n' for new calculation or type 'exit': ")
        if ip == 'yes':
            n1 = result 
        
        elif ip == 'n':
            clear()
            calculator() 
            break
        elif ip == 'exit':
            break
            


calculator()

num1 = 10
num2 = 10

def calculate (num1, operator,num2):
     if operator == "+":
        return (num1 + num2)
     elif operator == "-":
        return (num1 - num2)
     elif operator == "*":
        return (num1 * num2)
     elif operator == "/":
         return (num1 / num2)
     else:
        return "Invalid operator"

print(calculate(10, "+", 10))  
print(calculate(10, "-", 10))  
print(calculate(10, "*", 10))  
print(calculate(10, "/", 10)) 
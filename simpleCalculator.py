def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(base, exponent):
    return base ** exponent


print(add(23, 45))
print(multiply(23, 45))
print(divide(600, 45))
print(subtract(36, 20))
print(power(3, 4))

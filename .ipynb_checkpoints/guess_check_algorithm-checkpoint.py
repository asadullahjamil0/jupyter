def sqrt(x, guess = 0.0):
    if x < 0:
        return None
    if good_enough(guess, x):
        return guess
    else:
        new_guess = improve_guess(guess, x)
        return sqrt(x, new_guess)

def good_enough(guess, x):
    if abs(guess * guess - x) < 0.1:
        return True
    else:
        return False

def improve_guess(guess, x):
    if guess < x:
        return guess + 0.1
    else:
        return guess - 0.1

print(sqrt(4, 1.8))
print(sqrt(-2))        

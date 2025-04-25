## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x, guess = 0.0):
    if good_enough(guess, x):
        return guess
    else:
        new_guess = improve_guess(guess, x)
        return sqrt(x, new_guess)
    
#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####

def good_enough(guess, x):
    if abs(guess * guess - x) < 0.1:
        return True
    else:
        return False

def average(a, b):
    return (a + b) / 2.0

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(a, x):
    x = x * 1.0
    if a == 0.0:
        a += 0.1
    better_guess = average(a, x / a)
    return better_guess

#### End OF MARKER




if __name__ == '__main__':
    print(sqrt(36, 5))

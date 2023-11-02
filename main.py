# Required imports
# We import sys to return custom error messages
import sys
# Accumulator Object
# An overview of its functions can be found here:
# http://www.categories.acsl.org/wiki/index.php?title=Assembly_Language_Programming


class Accumulator:
    # Accumulator constructor
    def __init__(self):
        self.accumulator = [0]
    # Printing the Accumulator

    def __repr__(self):
        return str(self.accumulator)

    def __str__(self):
        return repr(self)
    # Loading to the Accumulator

    def load(self, val):
        self.accumulator.append(val)
        return self.accumulator
    # Storing the Accumulator's latest value into a variable

    def store(self, var):
        Var[var] = self.accumulator[-1]
    # Adding to the Accumulator

    def add(self, val):
        self.accumulator.append(self.accumulator[-1] + val)
        return self.accumulator
    # Overloading the addition operator for the Accumulator

    def __add__(self, val):
        return self.add(val)
    # Subtracting from the Accumulator

    def sub(self, val):
        self.accumulator.append(self.accumulator[-1] - val)
        return self.accumulator
    # Overloading the subtraction operator for the Accumulator

    def __sub__(self, val):
        return self.sub(val)
    # Mutliplying the Accumulator

    def mul(self, val):
        self.accumulator.append(self.accumulator[-1] * val)
        return self.accumulator
    # Overloading the multiplication operator for the Accumulator

    def __mul__(self, val):
        return self.mul(val)
    # Dividing the Accumulator

    def div(self, val):
        self.accumulator.append(self.accumulator[-1] / val)
        return self.accumulator
    # Overloading the division operator for the Accumulator

    def __truediv__(self, val):
        return self.div(val)


# Instantiating the Accumulator
Accumulator = Accumulator()
# Variables Dictionary
Var = {}
# This function allows the user to set values in the Variables Dictionary


def let(name, val):
    Var[name] = val
    return Var
# Takes the square root of x


def sqrt(x):
    return x**(1 / 2)
# Takes the absolute value of x


def abs(x):
    # The method is to take the principle root of the value's square, which
    # will return a positive number with magnitude equal to x
    return ((((x)**2)**(1 / 2)))
# Takes the signum value of x
# A reference on the signum function can be found here:
# https://mathworld.wolfram.com/Sign.html


def signum(x):
    return x / abs(x) if x != 0 else 0
# Determines the parity of x
# Parity refers to whether the number is even or odd
# In this implementation, non-integer values are odd


def parity(x):
    return 'Even' if x % 2 == 0 else 'Odd'


# Finds the factorial of x
# This list prevents recursion depth errors
# The idea is that if the function factorial(2000) is called, it will return a recursion error
# However, if we call factorial(1000), it will not return a recursion error, and will expand this list up to the factorial of 1000. Then we can call factorial(1500), and the same will happen up to 1500. Now, our list is big enough that we can call factorial(2000), and it will return the correct output, instead of a recursion error.
# This effectively reduces the recursion depth for each number.
factorials = [1, 1, 2, 6, 24, 120, 720, 5040]


def factorial(x):
    length = len(factorials)
    # If the number's factorial is in the list, return that factorial
    if x < length:
        return factorials[x]
    # Calculate the factorials and fill in the list until we reach the number
    else:
        factorials.append(factorial(x - 1) * x)
        return factorial(x - 1) * x


# Determines the fibonacci numbers
# This function is implemented similarly to the factorial function
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
             89, 144, 233, 377, 610, 987, 1597, 2584, 4181]


def fib(x):
    length = len(fibonacci)
    if x < length:
        return fibonacci[x]
    else:
        fibonacci.append(fib(x - 1) + fib(x - 2))
        return fib(x - 1) + fib(x - 2)
# Sorting a list using Insertion Sort


def sort(x):
    for i in range(1, len(x)):
        j = i
        curr = x[j]
        pre = x[j - 1]
        while curr < pre:
            x[j] = pre
            x[j - 1] = curr
            j -= 1
            if j == 0:
                break
            curr = x[j]
            pre = x[j - 1]
    return x
# Stalin Sort easter egg
# A reference on Stalin Sort can be found here:
# https://github.com/gustavo-depaula/stalin-sort


def stalinsort(x):
    length = len(x)
    _next = 0
    _return = []
    for i in range(1, length):
        if x[i] >= _next:
            _next = x[i]
            _return.append(x[i])
    return _return
# Finding the maximum of a list by iteration


def max(x):
    _return = x[0]
    for i in x:
        if i > _return:
            _return = i
    return _return
# Finding the minimum of a list by iteration


def min(x):
    _return = x[0]
    for i in x:
        if i < _return:
            _return = i
    return _return
# Polynomial Object


class Polynomial:
    # Polynomial Constructor
    def __init__(self, *coefficients):
        self.coeffs = list(coefficients)
    # Printing the Polynomial

    def __str__(self):
        string = ''
        j = len(self.coeffs) - 1
        for i in self.coeffs:
            if j > 1:
                string += str(i) + ' x**' + str(j) + ' + '
            else:
                string += str(i) + (j * ' x + ')
            j -= 1
        return string
    # Returns the coefficients of a Polynomial

    def coeff(self, i):
        return self.coeffs[len(self.coeffs) - 1 - i]
    # Adding two Polynomials

    def add(self, other):
        x = self.coeffs[::-1]
        y = other.coeffs[::-1]
        # Fills in 0's to lists if they're not the same size
        for _ in range(max([len(x), len(y)]) - min([len(x), len(y)])):
            if len(x) < len(y):
                x.append(0)
            elif len(y) < len(x):
                y.append(0)
            else:
                pass
        z = [a + b for a, b in zip(x, y)][::-1]
        # The star operator is used to unwrap the list z
        return Polynomial(*z)
    # Overloading the addition operator for Polynomials

    def __add__(self, other):
        return self.add(other)
    # Subtracting one Polynomial from another
    # The method is to change the second Polynomial's coefficient's signs and
    # then adding them

    def sub(self, other):
        x = [i for i in other.coeffs]
        for i in range(len(x)):
            x[i] /= -1
        return self.add(Polynomial(*x))
    # Overloading the subtraction operator for Polynomials

    def __sub__(self, other):
        return self.sub(other)
    # Multiplying the Polynomials by FOIL

    def mul(self, other):
        x = self.coeffs
        y = other.coeffs
        zd = {}
        inc = len(x) + len(y) - 2
        for i in reversed(range(inc)):
            zd[i + 1] = []
        for i in y:
            for j in x:
                try:
                    zd[inc].append(i * j)
                    inc -= 1
                except BaseException:
                    pass
            inc = len(x) + len(y) - y.index(i) - 3
        zd[0] = [x[-1] * y[-1]]
        return Polynomial(*[sum(i) for i in zd.values()])
    # Overloading the multiplication operator for Polynomials

    def __mul__(self, other):
        return self.mul(other)
    # Finding a specific coefficient in a Polynomial

    def val(self, other):
        value = []
        j = len(self.coeffs) - 1
        for i in self.coeffs:
            value.append(i * other**j) if j >= 1 else value.append(i)
            j -= 1
        return sum(value)
    # Overloading the call function for Polynomials to find a specific
    # coefficient

    def __call__(self, other):
        return self.val(other)
    # Finding the roots of a Polynomials
    # _min, _max, and prec are optional parameters
    # _min is the minimum of the Bisection Method, _max is the maximum of the Bisection Method, prec is how precise the Bisection Method will be
    # A reference on the Bisection Method can be found here:
    # https://en.wikipedia.org/wiki/Bisection_method

    def roots(self, _min=0, _max=2147483647, prec=1):
        # If the Polynomial is linear, the root is -b/a
        if len(self.coeffs) == 2:
            return [-self.coeffs[-1] / self.coeffs[0]]
        # If the Polynomial is quadratic, we employ the Quadratic Formula
        elif len(self.coeffs) == 3:
            return [((-self.coeffs[1] + ((self.coeffs[1]**2) - 4 * self.coeffs[0] * self.coeffs[-1])**0.5) / (2 * self.coeffs[0])),
                    ((-self.coeffs[1] - ((self.coeffs[1]**2) - 4 * self.coeffs[0] * self.coeffs[-1])**0.5) / (2 * self.coeffs[0]))]
        # Otherwise, we employ the Bisection Method in the interval [_min, _max]
        else:
            n = 1
            while n < prec * 1000:
                midpoint = (_min + _max) / 2
                if self(midpoint) == 0 or (_max - _min) / 2 < prec:
                    return midpoint
                n += 1
                if signum(self(midpoint)) == signum(self(_min)):
                    _min = midpoint
                else:
                    _max = midpoint
            return "Cannot calculate roots for higher order functions"
# Vector Object


class Vector:
    # Vector constructor
    def __init__(self, *components):
        self.components = [float(i) for i in list(components)]
        self.dimensions = len(list(components))
    # Printing the Vector

    def __str__(self):
        return str(tuple(self.components))
    # Returning the dimensions of the Vector

    def dimensions(self):
        return self.dimensions
    # Finding the Vector's component in a specific dimension

    def get(self, dim):
        return self.components[dim - 1]
    # Overloading the addition operator for Vectors

    def __add__(self, vector):
        # Check if the dimensions of both Vectors are the same
        if len(self.components) != len(vector.components):
            return "Error: The addends of vector addition must be in the same dimension"
        return Vector(*[self.components[i] + vector.components[i]
                      for i in range(len(self.components))])
    # Overloading the subtraction operator for Vectors
    # Works similarly to the Polynomial's subtraction function

    def __sub__(self, vector):
        if len(self.components) != len(vector.components):
            return "Error: The minuend and subtrahend of vector subtraction must be in the same dimension"
        _vector = Vector(*[-1 * i for i in vector.components])
        return self + _vector
    # Overloading the multiplication operator for Vectors

    def __mul__(self, multiple):
        # Multiply each component by the multiple
        _return = [i for i in self.components]
        for i in range(len(_return)):
            _return[i] *= multiple
        return Vector(*_return)
    # The addition function for Vectors

    def add(self, vector):
        return self + vector
    # The subtraction function for Vectors

    def sub(self, vector):
        return self - vector
    # The mutliplication function for Vectors

    def mul(self, multiple):
        return self * multiple


# Running the interpreter
def interpret():
    line = 0
    running = True
    while running:
        # Taking user input
        print(f'Line {line} : ', end='')
        _input = input()
        # If the user types the exit command, we System Exit
        if _input == 'exit()':
            running = False
        try:
            exec(f'print({_input})')
        # If there's an error, we print it in red using an ANSI color code
        except BaseException:
            e = sys.exc_info()[0]
            print('\033[91m' + str(e)[8:-2])
            print('\033[0m', end='')
        line += 1

if __name__ == "__main__":
    if len(sys.argv) == 3:
        sys.stdin = open(sys.argv[1], 'r')
        sys.stdout = open(sys.argv[2], 'w')
    elif len(sys.argv) == 2:
        sys.stdin = open(sys.argv[1], 'r')
    else:
        sys.stdin = sys.__stdin__
    interpret()

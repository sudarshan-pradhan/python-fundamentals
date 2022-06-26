####################################################

triple = lambda num : num * 3  # Assigning the lambda to a variable
print(triple(10))  # Calling the lambda and giving it a parameter

####################################################

concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
print(concat_strings("World", "Wide", "Web"))

####################################################

my_func = lambda num: "High" if num > 50 else "Low"
print(my_func(60))

####################################################

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function

result = calculator(multiply, 10, 20)
print(result)
print(calculator(add, 10, 20))

####################################################

def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function
# 10 and 20 are the arguments.
result = calculator(lambda n1, n2: n1 * n2, 10, 20)
# The lambda multiplies them.
print(result)
print(calculator(lambda n1, n2: n1 + n2, 10, 20))

####################################################

# The built-in map() function creates a map object using an existing list 
# and a function as its parameters. This object can be converted to a list 
# using the list() function (more on this later).

num_list = [0, 1, 2, 3, 4, 5]
double_list = map(lambda n: n * 2, num_list)
print(list(double_list))

####################################################

# The function will be applied, or mapped, to all the elements of the list.

numList = [30, 2, -15, 17, 9, 100]
greater_than_10 = list(filter(lambda n: n > 10, numList))
print(greater_than_10)

####################################################
# variable declaration, number initialized
num1 = 42
# variable declaration, decimal/float initialized
num2 = 2.3
# variable declaration, boolean initialized
boolean = True
# variable declaration, string initialized
string = 'Hello World'
# variable declaration, list initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# variable declaration, dictionary initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# variable declaration, tuple initialized
fruit = ('blueberry', 'strawberry', 'banana')
# print to console, type check
print(type(fruit))
# print to console, List access value
print(pizza_toppings[1])
# list add value
pizza_toppings.append('Mushrooms')
# print to console, Dictionary access value
print(person['name'])
# Dictionary change value
person['name'] = 'George'
# Dictionary change value
person['eye_color'] = 'blue'
# print to console, Tuple access data
print(fruit[2])
# Conditional if, evaluation, print to console, Conditional else, print to console
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# Conditional if - elif - else, print to console.
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# For Loop comienza en 0 y sube hasta 5
for x in range(5):
    print(x)
# For Loop comienza en 2 y sube hasta 5
for x in range(2,5):
    print(x)
# For loop comienza en 2,sube hasta 10, incrementa por 3
for x in range(2,10,3):
    print(x)

# While Loop, variable declaration
x = 0
while(x < 5):
    # printing to console
    print(x)
    # incrementing x
    x += 1

# Lista de valor de eliminación al final
pizza_toppings.pop()
# Lista el valor de eliminación en el índice
pizza_toppings.pop(1)

# print to console of dictionary
print(person)
# Dictionary delete value
person.pop('eye_color')
# print to console of dictionary
print(person)

# for loop recorre una lista
for topping in pizza_toppings:
    # Conditional if
    if topping == 'Pepperoni':
        #continues
        continue
    # print to console
    print('After 1st if statement')
    # Conditional if
    if topping == 'Olives':
        #stops the loop
        break

# function declaration
def print_hello_ten_times():
    #for loop comienza en 0 sube hasta 10
    for num in range(10):
        #print to console
        print('Hello')

# Function Call
print_hello_ten_times()

# function Declaration with parameter x
def print_hello_x_times(x):
    #For bucle hasta un numero dado x
    for num in range(x):
        # print to concole
        print('Hello')

# function llamada de argumento de 4
print_hello_x_times(4)

# function declaration con parametro por defecto
def print_hello_x_or_ten_times(x = 10):
    #For loop hasta x
    for num in range(x):
        #print to console
        print('Hello')

#Function la llamada va hasta 10
print_hello_x_or_ten_times()
# Function la llamada va hasta 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
# print to console
print(num3)
# variable declaration, number initialized
num3 = 72
# Dictionary change value
fruit[0] = 'cranberry'
# print to console, Dictionary access value
print(person['favorite_team'])
# print to console, Tuple access data
print(pizza_toppings[7])
# imprime T or F
print(boolean)
# list add value
fruit.append('raspberry')
# Dictionary delete value
fruit.pop(1)
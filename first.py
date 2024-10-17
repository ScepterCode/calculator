# x = 5
# print (x)

# y = 'Godspower'
# print (y)

# x = 5
# x = 10
# print (x)

# x = 'john'
# x =  10
# print (x)

# x = 1j
# y = 'run'
# z = 5.0


# #CASTING
# print(type(x))
# print(type(y))
# print(type(z))








#print ('hello')




# import time

# # Function to populate a list
# def populate_list(list_name):
#     user_list = []
#     while True:
#         item = input(f"indicate item {list_name}: ")
#         user_list.append(item)
#         done = input("Are you through? (yes/no): ").lower()
#         if done == 'yes':
#             break
#     return user_list


# name = input(f"Please enter your name:  ")
# age = int(input(f"Please enter your age: "))
# gender = input(f"Please enter your gender (male/female/other): ").lower()

# print (name)

# list1 = ["Name", "Age", "Gender"]
# list2 = ["John", "86", "male"]

# if len(list1) == len(list2):sceee
#     print("Length of list matches")
#     My_dict= dict(zip(list1, list2))
#     print("Dictionary created:", My_dict)
# else:
#     print("List doesn't Match")

#  Function to compare list lengths and print message accordingly
# def compare_lists(list1, list2):
#     if len(list1) != len(list2):
#         print("Length of lists don't match")
#         return False
#     else:
#         print("Lengths match. Proceeding", end="")
#         for _ in range(3):
#             time.sleep(1)
#             print(".", end="", flush=True)
#         print()
#         return True

# Main Program
# def main():
#     list1 = populate_list('list1')
#     list2 = populate_list('list2')


#     if compare_lists(list1, list2):
#         # create dictionary with list1 as keys and list2 as values
#         result_dict = dict(zip(list1, list2))
#         print("Dictionary created:")
#         print(result_dict)
# # 
# if __name__ == "__main__":
#     main()

# def friday(name):
#     print (f'{name} Thank God its friday!')
#     print ('Lets go party around town')




# friday('john')
# friday('John')
# friday('john')


# def multiply(a, b):
#     c = a * b
#     return c


# # print(multiply(2, 4))

# def fullname(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# create_name = fullname("power", "rangers")

# print(create_name)





# def spell(name, age):
#     print (f'hello {name} are you {age}')


# spell('john', '20')
# spell('james', '10')



# def multiply(a, b):
#     c = a * b
#     return c


 
# a =  int(input('enter your first number:  '))
# b = int(input('enter your second number:  '))

# print (multiply(a, b))


# def nation(country = ' nigeria'):
#     print('i am from' + country)


# nation(' india')
# nation(' china')
# nation()
# nation(' congo')


# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Create a dictionary to map operators to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Main program to use the calculator
def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

    # Get the corresponding function from the dictionary and execute it
    # if operation in operations:
    #     result = operations[operation](num1, num2)
    #     print(f"{num1} {operation} {num2} = {result}")
    # else:
    #     print("Invalid operation")

    # Use get() to retrieve the function or None if not found
    result = operations.get(operation, lambda x, y: "Invalid operation")(num1, num2)
    
    # Print the result
    print(f"{num1} {operation} {num2} = {result}")

# Call the calculator function
calculator()






































# Print the first ten natural numbers with or without a loop.
# Tip: Natural numbers are integers that start from 1.

# for number in range(1, 11):
#     print(number)



# Print the quotient and remainder when 9 is divided by 2.

# print(f"The quotient is {9 // 2}.")
# print(f"The remainder is {9 % 2}.")



# Print all the integers from 35 to 57 (including 35 and 57) except 47 and 50.

# for number in range(35, 58):
#     if number not in (47, 50):
#         print(number)



# Ask the user to enter two names of their choice. Check which of these two names have more number of letters. The one with the more number of letters
# should be printed in uppercase form. The other one should be printed in lowercase. If they have same number of letters, the program
# should print both the names in uppercase.
# For example:
# Enter the first name: Victor
# Enter the second name: Jasmine
# Output: victor JASMINE

# name_1 = input("Type in a name: ")
# name_2 = input("Type in a name: ")

# if len(name_1) < len(name_2):
#     print(name_1.lower(), name_2.upper())
# elif len(name_1) == len(name_2):
#     print(name_1.upper(), name_2.upper())
# else:
#     print(name_1.upper(), name_2.lower())



# Create a tuple of ten integers. Print the count of each integer using the count method.
# Tip: tuple_name.count(k) will give you the count of k in the tuple.

# from random import randint

# numbers = tuple(randint(1, 10) for _ in range(10))

# for number in numbers:
#     print(f"The count of {number} is {numbers.count(number)}.")



# Using a while loop, print the following pattern: 1 2 4 8 16 32 64 128 256 512
# Tip: Use the end argument if required.

# number = 1

# while number <= 512:
#     print(number, end=" ")
#     number *= 2



# Create a dictionary as shown below.
# data = {1: 'a', 2: 'b', 3: 'c'}
# Use string operations to join all the values of the dictionary and print the 
# resultant string in uppercase form. Expected output: 'ABC'

# data = {1: 'a', 2: 'b', 3: 'c'}

# values = list(data.values())
# result = ""

# for value in values:
#     result += value.upper()

# print(result)



# Store a sentence as a string. Use string operations to print every other word of this sentence starting from index 0.
# For example:
# sentence = "YoungWonks Online Coding Classes"
# Output:
# "YoungWonks Coding"

# sentence = "The world will last for five billion years"
# sentence = sentence.split()

# output = ""

# for index in range(0, len(sentence), 2):
#     output += sentence[index] + " "

# print(output)



# Create an empty list and put nine unique integers in the range 40 to 120 (including both end points) using the random module.
# Use a for loop to create a dictionary with the list indices as keys and list elements as values. Print the list and the dictionary.

# from random import randrange

# numbers = []
# numbers = [randrange(40, 121) for _ in range(9)]

# indices = {index: number for index, number in enumerate(numbers)}

# print(numbers)
# print(indices)



# Ask the user to enter an integer. If it is prime, print "You entered a prime number" otherwise print "You entered a composite number".
# Tip: A prime number is only divisible by 1 and itself.

# number = int(input("Enter a number: "))

# for divisor in range(2, number):
#     if number % divisor == 0:
#         print("You have entered a composite number.")
#         break
# else:
#     print("You have entered a prime number.")


# Holidays, Vacation, and Travel

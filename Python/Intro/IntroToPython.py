# Create a variable name and assign your name to it. 
# # Then, print a greeting message that includes your name.
# name = 'joey'
# print(f"Hello, " + name)

# # Assign the values 5 and 10 to two variables, and then 
# # print their sum, difference, product, and quotient.
# var1 = 5
# var2 = 10
# varSum = var1 + var2
# varDiff = var1 - var2
# varProd = var1 * var2
# varQuo = var1 / var2

# print(f"The Numbers {var1} and {var2}")
# print(f"Sum = {varSum}" + 
#       f" Diff = {varDiff}" +
#       f" Prod = {varProd}" +
#       f" Quo = {varQuo}")

# # Write a program that converts a given number of 
# # minutes to hours and minutes.
# def minToHour (minutes):
#     hours = minutes/60
#     return hours

# minutes = int(input("Enter the amount of minutes: "))
# print(f"The hour conversion for given minutes is: {minToHour(minutes)}")


# # Create a variable temperature and assign a float 
# # value representing a temperature in Celsius. 
# # Convert this temperature to Fahrenheit and print the result.
# # F = (9/5)C + 32.
# def convertCtoF (currentTempC):
#     currentTempF = (9/5 * currentTempC) + 32
#     return currentTempF

# currentTempC = int(input("Enter the temp in Cel: "))
# print(f"{currentTempC}C = {convertCtoF(currentTempC)}F")

# # Assign the string "Hello, World!" to a variable and print its length.
# messageStr = "Hello World!"
# print(len(messageStr))

# # Write a program that takes two integers from the user and prints their average.
# amtOfValues = int(input("Please enter the amount of values: "))
# allValues = []
# for _ in range(amtOfValues):
#       value = int(input("Enter a value: "))
#       allValues.append(value)

# divideBy = int(input("Enter the value to divide by: "))

# total = sum(allValues)
# average = total / divideBy

# print(f"The average is: {average}")
    
# ## for loop stuff
# # print each element in a list of numbers (numbers = [1, 2, 3, 4, 5])
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)

# # Print each character in a string.
# randomStringHere = "Well hey howdy"
# for letter in randomStringHere:
#     print(letter)

# # Print the first 10 natural numbers using range().
# for i in range(10):
#     print(i)

# # Calculate the sum of all numbers in a list. (numbers = [1, 2, 3, 4, 5])
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for number in numbers:
#     total += number
# print(total)

# # Find the maximum number in a list.
# numbers = [101, 1000, 9999, 2]
# highestNumber = 0

# for currentNumber in numbers:
#     if currentNumber > highestNumber:
#         highestNumber = currentNumber

# print (highestNumber)

# # Count the number of vowels in a string. (a, e, i, o, u.)
# vowels = ['a', 'e', 'i', 'o', 'u']
# randomString = "The quick brown fox jumps over the lazy dog"
# match = 0

# for letter in randomString:     
#     if letter in vowels:
#         match += 1

# print(match)

# # Print the squares of numbers from 1 to 10.
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in array:
#     squared = number * number
#     print(squared)

# # Iterate over a dictionary and print the key-value pairs.
# student_scores = {"Alice": 85, "Bob": 90, "Charlie": 78}

# for name, score in student_scores.items():
#     print(f"{name} scored an {score}")

# Print a multiplication table for a given number.
number = 5
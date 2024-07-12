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
#     currentTempF =(9/5 * currentTempC) + 32
#     return currentTempF

# currentTempC = int(input("Enter the temp in Cel: "))
# print(f"{currentTempC}C = {convertCtoF(currentTempC)}F")

# # Assign the string "Hello, World!" to a variable and print its length.
# messageStr = "Hello World!"
# print(len(messageStr))

# Write a program that takes two integers from the user and prints their average.
amtOfValues = int(input("Please enter the amount of values: "))
allValues = []
for _ in range(amtOfValues):
      value = int(input("Enter a value: "))
      allValues.append(value)

divideBy = int(input("Enter the value to divide by: "))

total = sum(allValues)
average = total / divideBy

print(f"The average is: {average}")
    

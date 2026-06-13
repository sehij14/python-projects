# Day4 Project
#Number Analyzer System

print("------NUMBER ANALYZER-----")

n = int(input("How many numbers do you want to enter? "))

even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0

for i in range(n):
    num = int(input("Enter number: "))
    
    # Even or Odd
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

#Positive or Negative
    if num  > 0:
         positive_count += 1
    elif num < 0:
        negative_count += 1

print("\n----RESULT----")
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)

print("----THANK YOU----")
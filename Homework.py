# Ex1 - String Enter text and display it one by one

# text = input("Enter your text: ")
# for i in range(len(text)):
#     print(text[i])

# # Ex2 - String Enter text and display number of letter..................

# text = input("Enter your text: ")
# for i in range(len(text)):
#     print(i)


# Ex3 - String
# Enter text and check if it contains capital letter or not 
# Display "Yes" if capital # display "No" if all lowercase letter

# text = input("Enter your text: ")
# index = 0
# result = "No"
# while index < len(text):
#     if text[index].isupper():
#         result = "Yes"
#         index = len(text)
#     index += 1  
# print(result)

# Ex4 - String .....................................................................      

# Q1 - display number 1 by one without space......

# text = "3 4 5 6"
# for i in range(len(text)):
#     if text[i] != " ":  
#         print(text[i])


# # Q2 - Sum all number (Total: 18).....
# text = "3 4 5 6"
# result = 0
# for char in text:
#     if char != " ":  
#         result += int(char)
# print(result)

# Ex5 - String .....................................................................      

# # Q1 - Count odd and even number in text....
# text = "454639"
# count_even = 0
# count_odd = 0
# for i in range(len(text)):
#     if i % 2 == 0:
#         count_even += 1
#     elif i % 2 == 1:
#         count_odd += 1
# print(count_even)
# print(count_odd)

# # Q2 - Sum all number ...............

# text = "454639"
# total = 0
# for i in range(len(text)):
#     total += int(text[i])
# print(total)

# # Q3 - Sum only even number ...........

# text = "454639"
# total = 0
# for i in range(len(text)):
#     if i % 2 == 0:
#         total  += 1
# print(total)

# # Q4 - reverse ....................

# text = "454639"
# reversed_text = ""
# for i in range(len(text)):
#     reversed_text += text[len(text) - 1 - i]
# print(reversed_text) 


# Ex6 - number ........Enter number and check, if odd number print "Odd" otherwise print "Even"

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Even number.")
# else:
#     print("Odd number.")

# Ex7 - number............................................

# isFound = False
# result = "Out of range!"
# while not isFound:
#     number = int(input("Enter a number: "))
#     if number >= 10 and number <= 20:
#         result = "Continue"
#         print(result)
#     else:
#         result = "Out of range!"
#         print(result)
#         isFound = True 

# Ex8 - sting..............................................

# Q1 - How many number 8 in string....
# text = "939488403988" 
# count_8 = 0
# for i in range(len(text)):
#     if text[i] == "8":
#         count_8 += 1
# print(count_8)

# Q2 - What is first index of letter 8...

# text = "939488403988"
# index = 0
# isFound8 = False
# while index < len(text) and not isFound8:
#     if text[index] == "8":
#         isFound8 = True
#     else:
#         index += 1
# if isFound8:
#     print(index)
# else:
#     print("8 not found")


# Ex9 - String....................................

# Q1 - Remove space and keep result = "3456"
# text = "3 4 5 6"
# output = ""
# for i in range(len(text)):
#     if text[i] != " ":
#         output += text[i]
# print(output)

# Q2 - Multiple each letter by 2 result = "6 8 10 12"

# string = "3 4 5 6"
# result = ""
# for char in string:
#     if char != " ": 
#         result += str(int(char) * 2)  + " "
# print(result)


# Ex10 - Number...................................
# Enter 5 numbers and find maximum and minimum value

# num1 = int(input("Number 1: "))
# max_value = num1
# min_value = num1
# for i in range(2, 6):
#     num = int(input("Number " + str(i) + ": ")) 
#     if num > max_value:
#         max_value = num
#     if num < min_value:
#         min_value = num
# print("Max: " , max_value)
# print("Min: " , min_value)




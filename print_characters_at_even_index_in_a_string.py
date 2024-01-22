#Exercise 3: Print characters from a string that are present at an even index number
#Write a program to accept a string from the user and display characters that are present at an even index number.

# Accept a string from the user
user_input = input("Enter a word:")
print("Original string is", user_input)

# Display characters at even index numbers
result = ''.join(user_input[i] for i in range(0, len(user_input), 2))

# Print the result
print("Characters at even index numbers:", ', '.join(result))



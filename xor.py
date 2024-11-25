# Define the string
input_string = "Hello world"

# XOR each character with 0 and display the result
result = ""
for char in input_string:
    result += chr(ord(char) ^ 0)

# Display the output
print("Original String:", input_string)
print("Result after XOR with 0:", result)
# Define the string
input_string = "Hello world"

# Perform AND operation with 127
and_result = "".join(chr(ord(char) & 127) for char in input_string)

# Perform XOR operation with 127
xor_result = "".join(chr(ord(char) ^ 127) for char in input_string)

# Display the results
print("Original String:", input_string)
print("Result after AND with 127:", and_result)
print("Result after XOR with 127:", xor_result)

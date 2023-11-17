def full_adder(a, b, carry_in):
    # Calculate sum
    sum_result = a ^ b ^ carry_in

    # Calculate carry
    carry_out = (a & b) | (carry_in & (a ^ b)) 
    return sum_result, carry_out
    
def add_binary_numbers(bits_a, bits_b):
    # Initialize variables
    result = [] 
    carry = 0

    # Perform addition using full_adder for each bit 
    for i in range(len(bits_a) - 1, -1, -1):
        sum_result, carry = full_adder(bits_a[i], bits_b[i], carry) 
        result.insert(0, sum_result)

    # If there's a final carry, add it to the result 
    if carry:
        result.insert(0, carry) 
        return result
    
def take_user_binary_input(bit_length):
    binary_input = input(f"Enter a {bit_length}-bit binary number: ")

    # Check if the input is a valid binary number
    if not binary_input.isdigit() or set(binary_input) - {'0', '1'}: 
        print("Please enter a valid binary number.")
        return take_user_binary_input(bit_length) 
    else:
        # Ensure the input is of the specified length 
        if len(binary_input) != bit_length:
            print(f"Please enter a {bit_length}-bit binary number.") 
            return take_user_binary_input(bit_length)
        else:
            return [int(bit) for bit in binary_input]

# Take 4-bit binary numbers from the user 
bit_length = 4
binary_a = take_user_binary_input(bit_length) 
binary_b = take_user_binary_input(bit_length)

# Perform addition
result = add_binary_numbers(binary_a, binary_b)

# Display the result
print(f"Binary Addition: {''.join(map(str, binary_a))} + {''.join(map(str, binary_b))} = {''.join(map(str, result))}")

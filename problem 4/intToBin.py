def int_to_reverse_binary(num1):
    binary_val = ''

    #Get binary digits for valid inputs
    while num1 > 0:
        binary_val = binary_val + str(num1 % 2)
        num1 = num1 // 2
    
    #For nonpositive inputs
    if binary_val == '':
        binary_val = '0'

    return binary_val


def string_reverse(input_string): 
    reverse_input = ''
    
    #Append characters in reverse
    for target in range(0,len(input_string)):
        reverse_input = reverse_input + input_string[len(input_string)-target-1]
    
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)
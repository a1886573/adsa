
#convert input to strings
data  = input()
#split the input where spaces are (into 3 parts in this case each for I1, I2 and B)
parts = data.split()

#then allocate those parts
I1 = parts[0]
I2 = parts[1]
B = int(parts[2])

def school_method_addition(number1, number2, base):

    max_length = max(len(number1), len(number2))
    number1 = number1.zfill(max_length)
    number2 = number2.zfill(max_length)

    carry = 0
    result = []
    
    #loop from max_length-1 (last digit) to index 0 (hence -1 to include it) and a step of -1 to descend
    for i in range(max_length -1, -1, -1):
        #setting a character of number 1 to a digit, starting from i (back)
        first_digit = int(number1[i])
        #setting a character of number 2 to a digit
        second_digit = int(number2[i])

        #adds the two digits plus a carry (either 0 or 1)
        digit_sum = first_digit + second_digit + carry
        
        #integer division to find whether a carry is needed for the next sum
        carry = digit_sum // base
        
        # this then gives the remainder of the sum, excluding a carry if applicable 
        digit = digit_sum % base
        
        #this digit is then added to the end of the result array
        result.append(str(digit))
    
    #after the for loop is completed if any carry remains (from the last operation) it is then added 
    if carry:
        result.append(str(carry))
    
    #Joins the indiviual strings and concentrates them into a single one 
    return ''.join(result[::-1])











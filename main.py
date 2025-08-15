#a1886573 Aidan Matkovic last edited 15/8/25: ADSA ASSIGNMENT 1

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

#pseudocode of this karatsuba implemention was found and further developed on from the course lecture slides
def karatsuba(a, b, B):

    a = str(a)
    b = str(b)

    # Base case: if either number is a single digit, multiply directly
    if len(a) == 1 or len(b) == 1:
        return int(a) * int(b)
    
    #size of subproblems
    n = max(len(a), len(b))
    k = n // 2
    
    #fill with zeros
    a = a.zfill(n)
    b = b.zfill(n)

    # Split numbers into high and low parts
    a1, a0 = a[:-k], a[-k:]
    b1, b0 = b[:-k], b[-k:]

    #initiating three different recursive steps (/subproblems) of the karatsuba algorithm
    P0 = karatsuba(a0, b0, B)
    P1 = karatsuba(a1, b1, B)

    sum1 = school_method_addition(a0,a1,B)
    sum2 = school_method_addition(b0,b1,B)
    P2 = karatsuba(sum1,sum2, B)

    #returning the final formula (corrected cross term)
    return P1 * B**(2*k) + (P2 - P1 - P0) * B**k + P0

    
#allowed to use any method of floor division (rounded down), assumed I2 is not 0
def division(number1, number2):
    num = number1
    denom = int(number2)
    result = []
    remainder = 0
    for digit in num:
        remainder = remainder * 10 + int(digit)
        result.append(str(remainder // denom))
        remainder %= denom
    
    # Remove leading zeros, return '0' if result is empty
    return ''.join(result).lstrip('0') or '0'


#set values for a and b, so need to convert I1 and I2 to integers
a =  int(I1)
b =  int(I2)

#call each function
school_addition_result = school_method_addition(I1, I2, B)
karatsuba_result = karatsuba(a,b,B)
division_result = division(I1,I2)

#printing out the results
print(school_addition_result, karatsuba_result, division_result)














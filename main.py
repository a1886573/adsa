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
def karatsuba(a, b, n):
    if n < 4:
        return a * b
    #size of subproblems 
    else:
        k = n // 2
    
        #by dividing the first number by its base to the power of k it gets the first (forward) section of the number
        a1 = a // B**k
        #And using the modulo operation we can get the back portion of the number
        a0 = a % B**k

        #same logic applied to partition number 2
        b1 = b // B**k
        b0 = b % B**k
   
        #initiating three different recursive steps (/subproblems) of the karatsuba algorithm
        P0 = karatsuba(a0,b0, k)
        P1 = karatsuba(a1,b1, k)
        P2 = karatsuba(a0+a1,b0+b1, k)

        #returning the final formula
        return P2 * B**(2*k) + (P1 - P2 - P0) * B**k + P0
    
#allowed to use any method of floor division (rounded down), simplest implementation is using // as given that b (aka I2) is non 0
def division(number1, number2):

    return number1 // number2


#set values for a and b, so need to convert I1 and I2 to integers
a =  int(I1)
b =  int(I2)
#set n to the max length of either a or b
n = max(len(I1), len(I2))

#call each function
school_addition_result = school_method_addition(I1, I2, B)
karatsuba_result = karatsuba(a,b,n)
division_result = division(a,b)

#printing out the results
print("Sum: ", school_addition_result)
print("Product: ", karatsuba_result)
print("Division: ", division_result)












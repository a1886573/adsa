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

#hinted at lectures to use school method multipliction when reached base case
def school_method_multiplication(number1, number2, base):
    #initialize a list to store the result
    result = [0]*(len(number1)+len(number2))
    #convert numbers to a list of digits (in reverse order which is easier for multiplication)
    number1 = [int(d) for d in number1[::-1]]
    number2 = [int(d) for d in number2[::-1]]
    
    #iterate through number 1
    for i in range(len(number1)):
        carry = 0
        #iterate through each digit of num 2
        for j in range(len(number2)):
            #multipy current digits and add current result and carry if applicable 
            sum = number1[i]*number2[j]+ result[i+j] + carry

            carry = sum // base
            result[i+j] = sum % base
        #if carry remains after loop add it to the next position
        if carry:
            result[i+len(number2)] += carry

    #remove leading zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return ''.join(str(d) for d in result[::-1])

#need to implement school subtraction for karatsuba function as well
def school_method_subtraction(a, b, base):
    #initialize a and b into list and pad with zeros so a and b are of the same length
    a = [int(x) for x in a.zfill(max(len(a), len(b)))]
    b = [int(x) for x in b.zfill(max(len(a), len(b)))]

    result = []
    borrow = 0
    
    #iterating from right to left
    for i in range(len(a)-1, -1, -1):
        #subtract a and b, account for the borrow
        sub = a[i] - b[i] - borrow

        #if negative need to borrow
        if sub < 0:
            sub += base
            borrow = 1
        else:
            borrow = 0

        result.append(str(sub))

    #reverse result to get into correct order
    result = ''.join(result[::-1]).lstrip('0')
    
    return result


#pseudocode of this karatsuba implemention was found and further developed on from the course lecture slides
def karatsuba(a, b):
    if len(a) == 1 or len(b) == 1:
        return school_method_multiplication(a, b, B)
    #calculate n as max length of a and b 
    n = max(len(a), len(b))

    k = n // 2
    #pad both a and b with zeros 
    a = a.zfill(n)
    b = b.zfill(n)

    #split a and b into 2 parts
    a1, a0 = a[:-k], a[-k:]
    b1, b0 = b[:-k], b[-k:]
    
    #need to calculate P0,P1 and P2 from karatsuba formula, best way to individually compute all additions/subtraction using school method
    P0 = karatsuba(a0, b0)
    P2 = karatsuba(a1, b1)

    sum1 = school_method_addition(a0, a1, B)
    sum2 = school_method_addition(b0, b1, B)
    P1 = karatsuba(sum1, sum2)

    P1_P2 = school_method_subtraction(P1, P2, B)
    P1_P2_P0 = school_method_subtraction(P1_P2, P0, B)
    
    #Multiply P2 by B^(2*k), shifts to left 
    P2_shifted = P2 + '0'*(2*k)
    
    #Multiply P2-P1-P0 by B^(k), shifts to left 
    P1_P2_P0_shifted = P1_P2_P0 + '0'*k

    result = school_method_addition(P2_shifted, P1_P2_P0_shifted, B)
    result = school_method_addition(result, P0, B)

    #remove leading zeros
    result = result.lstrip('0')

    return result


#call each function
school_addition_result = school_method_addition(I1, I2, B)
karatsuba_result = karatsuba(I1,I2)

#printing out the results
print(school_addition_result, karatsuba_result)














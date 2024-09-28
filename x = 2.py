# Oski Stole Your Power
from ctypes import string_at


def computePower (x,y):
    result = 1
    for i in range(y):
        #where i starts at 0, the range determines the maximum counter to go to not including itself
        result *= x
    #on first loop (i=0), takes result (1) and multiplies it by x (2). on second loop (i=1), takes result (2) and multiplies it by x (2). on third loop (i=2), takes result (4) and multiplies it by x (2). stops here because y=3 itself is not included in the range.
    #*= takes a value within a variable (in this case: result) multiplies it by a value (x) and reassigns the product as the new value for the variable
    return result

x = 2
y = 3
print (computePower (2,3))

# What Should I Wear?
def temperatureRange(readings):
    #readings is an input that is a list
    min_temp = min(readings)
    #take the minimum number from the list of readings
    max_temp = max(readings)
    #take the maximum number from the list of readings
    return (min_temp, max_temp)
    #return a list of 2 numbers--the minimum number and maximum number from the list of readings

readings = [50, 65, 78, 82, 88]
print(temperatureRange(readings))

# Check if its the Weekend
def weekendCheck(day):
    if day == 6 or day == 7:
        #where 6 is Saturday and 7 is Sunday
        return True 
    else:
        return False
    
print (weekendCheck(6))

# Fuel Efficiency Calculator
def fuel_efficiency(distance, fuel):
    efficiency = distance/fuel
    return efficiency

print (fuel_efficiency(70, 21.5))

# Secret Code (for 5-digit numbers only)
def decodeNumbers(n):
    #get the last digit of n
    last_digit = n % 10
    #remove last digit from n
    n //= 10
    rearranged = last_digit*10000
    return rearranged + n

print (decodeNumbers(12345))

# Secret Code
def decodeNumber2(n):
     #get the last digit of n
    last_digit = n % 10
    #remove last digit from n
    n //= 10
    
    #counter for number of digits in input (0 to #total)
    num_digits = 0
    # temporary variable for modified n (n wo last digit)
    temp = n
    while temp > 0: 
        temp //= 10
        #while the number is greater than 0, remove a digit off the end
        num_digits += 1
        #once the counter is finalized (after temp = 0 & the loop ends)
    return last_digit * (10 ** num_digits) + n 
    #the last digit multiplied by 10 to the power of the number of digits in the orignal input plus the modified n

# Min & Max but with Loops!

#For Loops
def find_min_with_for_loop(nums):
    min_value = nums[0]
    #assume the minimum value is the first number in the list for now
    for num in nums:
        if num < min_value:
            # if another number is less than the assumed minimum value then reassign that number as the new minimum value
            min_value = num
    return min_value

print(find_min_with_for_loop([7, 2, 3, 4, 5, 6, 1, 8]))

def find_max_with_for_loop(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value

print (find_max_with_for_loop([7, 2, 3, 4, 5, 6, 1, 8]))

# While Loops
def find_min_with_while_loop(nums):
    min_value = nums[0]
    index = 1
    #assume that the first value in the list is the minimum, then start indexing through the list starting at the second number

    while index < len(nums):
        #len counts the number of characters in a list--in this case it's the number of numbers
        if nums[index] < min_value:
            min_value = nums[index]
            #if any number in the list is smaller than the assumed smallest value (the first one) it becomes the new smallest value
        index += 1
        #while the index is less than the number of numbers in the list, the function above happens. each time it loops, the index is reassigned as itself + 1 until it reaches the number of numbers in the list.
    return min_value

print (find_min_with_while_loop([7, 2, 3, 4, 5, 6, 1, 8]))

def find_max_with_while_loop(nums): 
    max_value = nums[0]
    index = 1

    while index < len(nums):
        if nums[index] > max_value:
            max_value = nums[index]
        index += 1
    return max_value

print (find_max_with_while_loop([7, 2, 3, 4, 5, 6, 1, 8]))

# Counting Vowels
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    #classifying what vowels are
    vowel_count = 0
    consonant_count = 0
    #for now, set both vowel and consonant counts to 0 before going thru string

    for char in text:
        #defining char as one character in the text, which is the inputted string
        if char.isalpha():
            #if the character is in the roman alphabet
            if char in vowels:
                #then if the character is what is classified as a vowel, add one to the vowel count
                vowel_count += 1
            else:
                consonant_count += 1
                #if it is not what is classified as a vowel, add one to the consonant count
    return (vowel_count, consonant_count)

print (vowel_and_consonant_count("UC Berkeley, founded in 1868!"))

# Calculate Digital Root (I don't understand why can't I turn the number into a string and use range? pls help)
def digital_root(num):
    num = abs(num)
    #convert thru absolute value to make sure that the number is a positive number
    digit_sum = 0
    #assume that the digital sum is 0 before going through for loop
    for digit in str(num):
        #for every digit in the integer where str makes the integer into a string
        digit_sum += int(digit)
        #add the integer version of the digit to the digital sum
        #this loop keeps going until you run out of digits 

    return digit_sum

print (digital_root(12345))
 






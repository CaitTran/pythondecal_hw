#Hw4

#Debugging 

#Practicing Slicing & Striding

#2.1 Making a List Variable
num_list_totwenty = [i for i in range(0,21)]
print(num_list_totwenty)


num_list_totwenty_ver2 = [i for i in range (21)]
print(num_list_totwenty_ver2)
#the 0 is omitted bc i automatically starts at 0 in the range i=initial to 21, not including 21)

#2.2 Working with List Elements
def square(x):
    return x**2

def squareList(num_list):
    return list(map(square, num_list))

square_of_num_list = squareList(num_list_totwenty)
print(square_of_num_list)

"""list is defined as a variable whereas 2 is an integer. 
So, I can't square list because it is not an integer like 2.
So I tried to define it as x so that I could square it by two, but that just made the result a repeat of list of 0-20.
In the demo we used map to apply a function to every item in the list, and map is formated like (function, list)
So I defined a function (square) that squares an input, and in squareList i define x as a list (num_list). 
Since map only returns a tuple (n1, n2, n3, n... etc.), I used the list function to make the tuple returned back into a list.
"""

#2.3 Slicing

sliced_list_from_og_and_squared = squareList(num_list_totwenty)

def first_fifteen_elements(num_list2):
    return num_list2[0:15]

answer = first_fifteen_elements(sliced_list_from_og_and_squared)
print(answer)

"""originally i used for i in range (0,16) to return the first fifteen elements.
This doesn't work because 1. The range 0-16 is 17 elements. 
This also doesn't work because 2. The slice function is x[n1:n2]   :
Where x is the input (num_list2, which stands for any list).
Where n1 is the starting index and n2 is the final index.
I also didn't make answer = first_fifteen_elements(num_list2). This makes it so the inteded output is never spat out.
So the final version is a function first_fifteen_elements(x) that takes lists (num_list2). 
The function returns the input but sliced to start from the 0th index to the 15th index (15 elements).
Then, the result is given by making answer equal to this function taking the specific list indicated at the top.
The result becomes the output when I put it into the print function. I could've had this all in one line but for clarity sake, I put it separately.
"""
#2.4 Striding
#Slicing syntax with striding: [<start>:<end>:step], where step is the stride--how many indexes each step is

stride_every_fifth_element = squareList(num_list_totwenty)

def every_fifth_element(num_list3):
    return num_list3[::5]

answer2 = every_fifth_element(stride_every_fifth_element)
print(answer2)

#2.5 Slicing & Striding

pain_in_my_butt = squareList(num_list_totwenty)

def fancy_function(num_list4):
    return num_list4[20:0:-3]

answer3 = fancy_function(pain_in_my_butt)
print(answer3)

"""Initially this returned an empty list when I did:
pain_in_my_butt = squareList(num_list_totwenty)

def fancy_function(num_list4):
    return num_list4[-31:-1:-3]

answer3 = fancy_function(pain_in_my_butt)
print(answer3)

The error is that there aren't more than 20 elements in the list provided in Part 2.2, so doing 31 and 1 would be incorrect.
Additionally, the most optimal way to go in reverse order is only to negate the steps, so make the <start> and <stop> value positive;
Plus you start at the 20th index and end at the 0th index. IDK why if you start at 0th index and end at 20th index you get an empty list?
"""

#3 3D Lists

#3.1 Creating a 5x5 2D List
#A nested loop is a loop with another loop inside of it

num_list_to_twentyfive = [i for i in range(0,26)]

def create_2d_list(num_list5):
    giant_list_matrix = []
    index = 1 #index will stand as the individual numbers that will fill the matrix

    for row in range(1,6): #the for loop iterates over the range [1-5] (runs five times)
        list_matrix = [] #each iteration, a row will be created

        for columns in range(1,6): #within a row, another for loop iterates over the range [1-5] -- fills in individual numbers in the row until the range reaches 5 -- (this also runs five times)
            list_matrix.append(index) 
            index += 1 #every time a new number is added to the matrix, the index moves onto the next number (1, 2, 3, 4, ..., 25)
        giant_list_matrix.append(list_matrix) #when done filling out with 5 numbers, the row (called list_matrix) is added to the giant matrix
        
    return giant_list_matrix #when the giant matrix has been added with 5 rows (list_matrix's) / when the bigger for loop has run 5 times, the function returns the finished giant matrix.

matrix = create_2d_list(num_list_to_twentyfive)
print(matrix)

#3.2 Replacing 2D List with Multiples of 3

def modify_2d_list(any_matrix):
    modified_matrix = [] #big modified matrix

    for row in any_matrix: #for each preexisting row in the inputted matrix
        modified_list_matrix = [] #initialize a new modified list matrix (each row to be added to the big modified matrix; since there are only 5 preexisting rows, only 5 modified list matrices will be created) 
        
        for columns in row: #where columns stands for the numbers in the row (since there are only 5 preexising columns, only 5 modified columns will be made for each modified row).
            if columns % 3 == 0: #if the columns (number) is divisible by 3 wo leaving a remainder
                modified_list_matrix.append("?") 
            else: #if it isn't then leave it
                modified_list_matrix.append(columns) 
        
        modified_matrix.append(modified_list_matrix)
    return modified_matrix

print(modify_2d_list(matrix))

"""
I initially started with index again (I initialized index outside of the big for loop and index += 1 inside the smaller for loop like the last function).
But that gave me a matrix where every number divisible by 3 evenly was '?' BUT every number had its own row so that wasn't working..
I thought index was supposed to be used to represents the values to be inputted, so that's what I had in place of columns in the modulus operator (index % 3 == 0).
But after that didn't work I realized columns is because in the prev. function, every column becomes assigned a number value that index was used to input. so then columns was the right variable to use to refer to the numbers.
"""

#3.3 Summing None-'?' Elements

modified_2d_matrix = modify_2d_list(matrix)

def sum_non_question_elements(modified_2d_matrix):
    sum = 0 
    for row in modified_2d_matrix:
        for num in row:
            if num != '?':
                sum += num

    return sum

print(sum_non_question_elements(matrix))

"""
I originally didn't specify that I wanted to look at the individual columns (numbers) in the matrix so i only had one for loop that wrongly indicated num as the columns (number) when it was actually the rows of the matrix.
So I added another for loop to specify.
"""
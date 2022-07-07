# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
  return max([a,b,c])

print(max_num(1,2,3))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(num_list):
    if(len(num_list) == 0):
        return 0
    result = 1

    for i in num_list:
        result*=i
    return result

print (mult_list([1,2,3,4]))
# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]

print(rev_string("dog"))

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(a,b,c):
    return a in range(b,c+1)

print(num_within(5,6,7))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. 
# Each number is the two numbers above it added together.
def pascal(n):

    print("Pascal Triangle for",n,"rows:")

    row = []
    prev_row = []

    prev_row.append(1)
    prev_row.append(1)

    if (n <= 0): return

    print("1")
    if (n == 1):
        return

    print("1  1")
    if (n == 2):
        return

    current_row_len = 2

    for j in range (2,n):

        row.append(1)
        print("1", end = "")

        for i in range (1, current_row_len):
            pascal_num = prev_row[i-1] + prev_row[i] 
            print(" ",pascal_num, end = "")
            row.append(pascal_num)

        row.append(1)
        print("  1")

        prev_row = row
        row = []

        current_row_len += 1

    return

print(pascal(5))
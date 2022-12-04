# write a python function to find the max. of three numbers.
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest


res = maximum(5, 26, 87)
print("Largest Number: ", res)

def maximum_element(sequence, n):
    #build base case
    if n > len(sequence):
        return "Number exceeds maximum elements of the sequence, try again."
    elif n == len(sequence):
        return n
    else:
        return maximum_element(sequence, n + 1)

sequence = [1,3,5,7,9]
n = 6
test = maximum_element(sequence, n)
print(test)







def isValidSubsequence(array, sequence):
     # Initialize two index variables to keep track of the current index of both arrays.
    arr_index = 0
    seq_index = 0
     # Iterate over the array and the sequence arrays using the index variables.
    # The loop should run until we reach the end of either array or until we find all the elements of the sequence.
    while arr_index < len(array) and seq_index < len(sequence):
         # Check if the current element in the array matches the current element in the sequence.
        if array[arr_index] == sequence[seq_index]:
             # If the elements match, move to the next element in the sequence.
            seq_index += 1
             # In either case, move to the next element in the array.
        arr_index += 1
    
    return seq_index == len(sequence)

input_array = [5, 1, 22, 25, 6, -1, 8, 10]
input_sequence = [1, 6, -1, 10]
result = isValidSubsequence (input_array, input_sequence)
 # If we have reached the end of the sequence, it is a valid subsequence of the array.
    # Return True, otherwise return False.
print(result)
import random
import time
import sys

# Increase the recursion depth limit (adjust as needed)
sys.setrecursionlimit(10**6)  # Set to a higher value than the default

# Define the Merge Sort algorithm
def merge_sort(arr):
    # If the array has one element or is empty, return it
    if len(arr) <= 1:
        return arr
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    # Merge the sorted halves
    return merge(left_half, right_half)

# Merge function to merge two sorted arrays
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to find the kth smallest element using Merge Sort
def kth_smallest_merge_sort(arr, k):
    # Sort the array using Merge Sort
    start_time = time.time()  # Start time measurement
    sorted_arr = merge_sort(arr)
    end_time = time.time()  # End time measurement
    elapsed_time = end_time - start_time  # Calculate elapsed time
    # Return the kth smallest element and the elapsed time
    return sorted_arr[k-1], elapsed_time

# Generate a random array of 10 input values ranging from 0 to 100
input_values = [random.randint(0, 100) for _ in range(10)]
print("Input Array:", input_values)
k = 1  # Example value of k
result, time_taken = kth_smallest_merge_sort(input_values, k)
print(f"{k}th Smallest Element:", result)
print("Time Taken:", time_taken, "seconds")

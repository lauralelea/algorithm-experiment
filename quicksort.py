import random
import time
import sys

# Increase the recursion depth limit (adjust as needed)
sys.setrecursionlimit(10**6)  # Set to a higher value than the default

# Define the Quicksort algorithm
def quick_sort(arr):
    # If the array has one element or is empty, return it
    if len(arr) <= 1:
        return arr
    else:
        # Choose the first element as the pivot
        pivot = arr[0]
        # Partition the array into elements less than or equal to the pivot
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        # Partition the array into elements greater than the pivot
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        # Recursively sort the partitions and concatenate them
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Function to find the kth smallest element using Quicksort
def kth_smallest_quick_sort(arr, k):
    # Sort the array using Quicksort
    start_time = time.time()  # Start time measurement
    sorted_arr = quick_sort(arr)
    end_time = time.time()  # End time measurement
    elapsed_time = end_time - start_time  # Calculate elapsed time
    # Return the kth smallest element and the elapsed time
    return sorted_arr[k-1], elapsed_time

# Generate a random array of 10 input values ranging from 0 to 100
input_values = [random.randint(0, 100) for _ in range(10)]
print("Input Array:", input_values)
k = 1  # Example value of k
result, time_taken = kth_smallest_quick_sort(input_values, k)
print(f"{k}th Smallest Element:", result)
print("Time Taken:", time_taken, "seconds")

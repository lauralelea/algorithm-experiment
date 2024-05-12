import random
import time
import sys

# Increase the recursion depth limit (adjust as needed)
sys.setrecursionlimit(10**6)  # Set to a higher value than the default

# Define the Bubblesort algorithm
def bubble_sort(arr):
    # Iterate through the array
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Function to find the kth smallest element using Bubblesort
def kth_smallest_bubble_sort(arr, k):
    # Sort the array using Bubblesort
    start_time = time.time()  # Start time measurement
    sorted_arr = bubble_sort(arr)
    end_time = time.time()  # End time measurement
    elapsed_time = end_time - start_time  # Calculate elapsed time
    # Return the kth smallest element and the elapsed time
    return sorted_arr[k-1], elapsed_time

# Generate a random array of 10 input values ranging from 0 to 100
input_values = [random.randint(0, 100) for _ in range(10)]
print("Input Array:", input_values)
k = 1  # Example value of k
result, time_taken = kth_smallest_bubble_sort(input_values, k)
print(f"{k}th Smallest Element:", result)
print("Time Taken:", time_taken, "seconds")

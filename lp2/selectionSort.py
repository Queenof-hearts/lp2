# 🔹 Selection Sort – Code Explanation in Points
# Purpose:
# This code implements the Selection Sort algorithm to sort a list of integers in ascending order.

# 🔸 Step-by-Step Breakdown
# Function Definition:

# selectionSort(arr, size): Sorts the array arr of given size.

# Outer Loop (i):

# Iterates through each position in the array.

# Assumes the current position i holds the minimum.

# Inner Loop (j):

# Searches the rest of the array (i+1 to size-1) for a smaller value than arr[min_index].

# Swapping:

# If a smaller value is found, its index is stored.

# After the inner loop, swap the smallest found element with the current element at index i.

# User Input Section:

# Accepts number of elements.

# Accepts each element from the user to form the input array.

# Output:

# Displays the array before and after sorting.

# 🔸 Example
# Input:

# yaml
# Copy
# Edit
# enter no. of elements in array: 4  
# enter element 1: 64  
# enter element 2: 25  
# enter element 3: 12  
# enter element 4: 22  
# Output:

# csharp
# Copy
# Edit
# [64, 25, 12, 22]  
# after sorting:  
# [12, 22, 25, 64]
# 🔸 Time Complexity
# Best, Average, Worst: O(n²)

# Space Complexity: O(1) (in-place sort)

# Let me know if you want this explained with a dry run or diagram.

def selectionSort(arr,size):
    for i in range(size):
        min_index=i
        for j in range(i+1,size):
            if arr[j]<arr[min_index]:
                min_index=j
        (arr[i],arr[min_index])=(arr[min_index],arr[i])
 
arr=[]
n=int(input("enter no. of elements in array: "))
for i in range(n):
    num=int(input(f"enter element {i+1}: "))
    arr.append(num)
print(arr)
selectionSort(arr,n)
print("after sorting: ")
print(arr)

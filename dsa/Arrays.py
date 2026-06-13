# Arrays
'''1)Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
Note: The second largest element should not be equal to the largest element. len() always consider index from 1 not 0 like list'''

def second_largest(arr):
    if len(arr) < 2: # If the array has less than 2 elements, return -1
        return -1
    first = second = -1
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second
'-------------------OR------------------'
# Example usage:
arr = [12, 35, 1, 10, 34, 1]
#print(second_largest(arr))  # Output: 3

# 2nd Example usage:
class Solution:
    def getSecondLargest(self, arr):
        arr=sorted(set(arr),reverse=True)
        len_arr=len(arr)
        if len_arr < 2:
            arr=-1
        else:
            arr=arr[1]
            
        return arr
sol = Solution()
print(sol.getSecondLargest(arr))  # Output: 34

"-----------------------------------------------------------------------------"
'''2)You are given an array arr[] of non-negative integers. You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, 
     meaning you should not use extra space for another array.'''

class Solution:
    def move_zeros_to_end(self,arr):
        n = len(arr)
        count = 0  # Count of non-zero elements (count is index of next)

    # Traverse the array. If element is non-zero, then
    # replace the element at index 'count' with this element
        for i in range(n):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1

    # Now all non-zero elements have been moved to the front
    # and 'count' is set as index of first 0. Make all
    # elements 0 from count to end.
        while count < n:
            arr[count] = 0
            count += 1
        return arr
    
# Example usage:
arr = [1, 2, 0, 4, 3, 0, 5, 0] # Output: [1, 2, 4, 3, 5, 0, 0, 0]
sol = Solution()
print(sol.move_zeros_to_end(arr)) 

'-------------------------------------or----------------------------------------'
def move_zeros_to_end(arr):
    for i in arr:
        if i == 0:
            arr.remove(i) #remove zero from array
            arr.append(i) #append zero at last
    return arr
# Example usage:
arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(move_zeros_to_end(arr))  # Output: [1, 2, 4, 3, 5, 0, 0, 0]

'-------------------------------------or----------------------------------------'
def move_zeros_to_end(arr):
    insert=0
    for i in range(len(arr)): #traverse the array
        if arr[i]!=0: #non zero element
            arr[insert]=arr[i] #put non zero element at insert index
            insert+=1
    while insert<len(arr):
        arr[insert]=0
        insert+=1
    return arr
# Example usage:
arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(move_zeros_to_end(arr))  # Output: [1, 2, 4, 3, 5, 0, 0, 0]
'------------------------------or---------------------------------------------'
def move_zeros_to_end(arr):
    insert=0 #insert means jaha pe next non zero element jayega
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[insert],arr[i]=arr[i],arr[insert]
            insert+=1
    return arr
# Example usage:                    
arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(move_zeros_to_end(arr))  # Output: [1, 2, 4, 3, 5, 0, 0, 0]

"-----------------------------------------------------------------------------"
'''n-1-i (reverse---i ke jagah 2,3,4)'''
'''3)Given an array, write a function to reverse the array.'''

def reverse_array(arr):
    start = 0 #start means left of array
    end = len(arr) - 1 #end means right of array
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
# Example usage:
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))  # Output: [5, 4, 3, 2, 1]

'''---------------------------------------------------------------------------'''
"Remainder = modulus except negative sign"
'''4)Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.'''
#Right rotation
def rotate_array(arr, d):
    n=len(arr) # Length of the array 5
    rotations=d%n # Handle cases where d >= n (2%5=2)
    
    for i in range(rotations):
        e=arr.pop() # Remove the last element
        arr.insert(0,e) # Insert it at the beginning of the array
    return arr
# Example usage:        
arr = [1, 2, 3, 4, 5]
d = 2
print(rotate_array(arr, d))  # Output: [4, 5, 1, 2,3]

#left rotation
def rotate_array(arr, d):
    n=len(arr) # Length of the array 5
    rotations=d%n # Handle cases where d >= n (2%5=2)
    
    for i in range(rotations):
        e=arr.pop(0) # Remove the first element
        arr.append(e) # Append it to the end of the array
    return arr
# Example usage:
arr = [1, 2, 3, 4, 5]
d = 2
print(rotate_array(arr, d))  # Output: [3, 4, 5, 1, 2]

'----------------------OR-----------------------'
def rotate_array(arr, d):
    n = len(arr) # Length of the array 5
    k = d % n  # Handle cases where d >= n (2%5=2)
    #arr[:] = arr[n-k:] + arr[:n-k] #Right rotation last ke 2 samne # Rotate the array in place (n-k 5-2=3,3 se chalu hoga phir + n-k tak)
    arr[:] = arr[k:] + arr[:k] #Left rotation first ke 2 last me # Rotate the array in place (n-k 5-2=3,0 se 3 tak hoga phir + 3 se end tak)
    return arr
# Example usage:
arr = [1, 2, 3, 4, 5]
d = 2
print(rotate_array(arr, d))  # Output: [3, 4, 5, 1, 2]

'----------------------OR--------------------------'
'without using slicing'
def rotate_array(arr, d):
    n = len(arr) # Length of the array 5
    d = d % n  # Handle cases where d >= n (2%5=2)
    k = n - d  # Calculate the effective rotation point (5-2=3)

    # Helper function to reverse a portion of the array
    def reverse(left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


    # Reverse the first last k elements (index 3 se end tak)
    reverse(n - k, n - 1) #3 se 4 tak
    # Reverse the remaining elements (0 se index 3 tak)
    reverse(0, n - k - 1) #0 se 2 tak
    # Reverse the entire array to achieve the final rotated state
    reverse(0, n - 1)

    return arr
# Example usage:
arr = [1, 2, 3, 4, 5]
d = 2
print(rotate_array(arr, d))  # Output: [3, 4, 5, 1, 2]

'''------------------------------------------------------------------------------'''
'''5)Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

Note:  A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order'''
#sometime we use brute force method to solve this type of question

def next_permutation(arr):
    n = len(arr) # Length of the array
    i = n - 2 # Start from the second last element

    # Step 1: Find the first decreasing element from the right
    while i >= 0 and arr[i] >= arr[i + 1]: #
        i -= 1

    if i >= 0:
        # Step 2: Find the element just larger than arr[i] to its right
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        # Step 3: Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]

    # Step 4: Reverse the elements to the right of index i
    left, right = i + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
# Example usage:
arr = [1,  2,  3,  6,  5,  4]
print(next_permutation(arr))  # Output: [1, 2, 4, 3, 5, 6]
'--------------------------------------------------------------------------'

'''6)Given an array arr[] consisting of n integers, the task is to find all the array elements which occurs more than floor(n/3) times.

Note: The returned array of majority elements should be sorted.'''

def majority_elements(arr):
    n = len(arr) # Length of the array
    threshold = n // 3 # Calculate floor(n/3)
    frequency = {} # Dictionary to store frequency of elements
    result = [] # List to store majority elements

    # Count the frequency of each element
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1 # Increment the count for num

    # Find elements that occur more than floor(n/3) times
    for num, count in frequency.items(): # Iterate through frequency dictionary
        if count > threshold: # Check if count exceeds threshold
            result.append(num) # Sirf num append karna hai count nahi.

    return sorted(result)  # Return the result sorted
# Example usage:
arr = [3, 2, 3] # Output: [3]

'--------------------------------OR----------------------------------------'
def majority_elements(arr):
    if not arr:
        return []
    n = len(arr) # Length of the array
    threshold = n // 3 # Calculate floor(n/3)
    arr.sort() # Sort the array to group identical elements together
    result = [] # List to store majority elements
    count = 1 # Initialize count for the first element

    # Traverse the sorted array to count occurrences of each element
    for i in range(1, n): # Start from the second element
        if arr[i] == arr[i - 1]: # If current element is same as previous
            count += 1 # Increment the count
        else:
            if count > threshold: # Check if count exceeds threshold
                result.append(arr[i - 1]) # Append the previous element to result
            count = 1 # Reset count for the new element

    # Check the last element's count after the loop
    if count > threshold:
        result.append(arr[-1]) # Append the last element if it exceeds threshold

    return sorted(result)  # Return the result sorted
# Example usage:
arr = [3, 2, 3] # Output: [3]

'--------------------------------------------------------------------------------------'
'''7)The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.'''
'multiple transaction allowed by greedy approach need to sell before buy multiple profits add at the end'
def max_profit(prices):
    total_profit = 0 # Initialize total profit to 0

    # Traverse the price array
    for i in range(1, len(prices)): # Start from the second day
        if prices[i] > prices[i - 1]: # If today's price is greater than yesterday's
            total_profit += prices[i] - prices[i - 1] # Add the profit to total profit

    return total_profit # Return the total profit
# Example usage:
prices = [100, 180, 260, 310, 40, 535, 695] #(180-100)+(260-180)+(310-260)+(535-40)+(695-535)=80+80+50+495+160=865
print(max_profit(prices))  # Output: 865
# Example usage:
prices = [1, 2, 3, 4, 5]
print(max_profit(prices))  # Output: 4

'-------------------OR------------------'

'single transaction allowed'
def max_profit(prices):
    n = len(prices) # Length of the price array
    max_profit = 0 # Initialize maximum profit to 0
    min_prices = float('inf') # Initialize minimum price to infinity
    # Traverse the price array
    for i in range(0,n):
        min_prices= min(min_prices,prices[i]) # Find the minimum price so far
        max_profit= max(max_profit,prices[i]-min_prices) # Calculate the maximum profit
    return max_profit # Return the maximum profit
# Example usage:
prices = [100, 180, 260, 310, 40, 535, 695]
print(max_profit(prices))  # Output: 655
# Example usage:
prices = [1, 2, 3, 4, 5]
print(max_profit(prices))  # Output: 4

'-------------------------------------------------------------------------------'
'''8)Given an array arr[] denoting heights of n towers and a positive integer k.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by k
Decrease the height of the tower by k
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by k for each tower. After the operation, the resultant array should not contain any negative integers.'''

def get_min_diff(arr, n, k):
    # Sort the array
    arr.sort()

    #We must minimize: max_height - min_height (sorted array me last - first means max - min)
    # Initial difference
    ans = arr[-1] - arr[0]

    # Initialize smallest and largest
   
    small = arr[0] + k
    big = arr[-1] - k

    # Traverse through array
    for i in range(n - 1):
        subtract = arr[i] - k
        add = arr[i + 1] + k

        # Skip if subtraction leads to negative height
        if subtract < 0:
            continue

        # Find min and max heights after modification
        min_height = min(small, add) # compare previous smallest after adding k to next element
        max_height = max(big, subtract) # compare previous bigger after subtracting k to other element

        # Update the minimum difference
        ans = min(ans, max_height - min_height)

    return ans
# Example usage:
arr = [1, 5, 8, 10] # Output: 5
k = 2
n = len(arr)
print(get_min_diff(arr, n, k))  # Output: 5

# Example usage:
arr = [3, 9, 12, 16, 20] # Output: 11
k = 3
n = len(arr)
print(get_min_diff(arr, n, k))  # Output: 11
'-------------------OR------------------'
'sometime taking i+1 and i-1 is not better use arr[i] - k and arr[i-1] + k. It is less error-prone than the i vs i+1 variant.'
def minimize_height_difference(arr, k):
    n = len(arr)
    if n == 1:
        return 0

    arr.sort()

    # Initial difference
    ans = arr[-1] - arr[0]

    # After modifying extremes
    small = arr[0] + k
    big = arr[-1] - k

    # Ensure small is actually the smaller of the two after initial estimate
    if small > big:
        small, big = big, small

    # Iterate through array and consider arr[i] as the first element of the right partition
    for i in range(1, n):
        # If arr[i] < k then arr[i] - k would be negative; skip such i
        if arr[i] < k:
            continue

        # Candidate min is min(small, arr[i] - k)
        # Candidate max is max(big, arr[i-1] + k)
        min_height = min(small, arr[i] - k)
        max_height = max(big, arr[i-1] + k)

        ans = min(ans, max_height - min_height)

    return ans # Return the minimum possible difference
# Example usage:
arr = [1, 5, 8, 10] # Output: 5
k = 2
print(minimize_height_difference(arr, k))  # Output: 5

'''9)You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

Note : A subarray is a continuous part of an array.'''
#subarray means contiguous part of array
#we have to find possible starting and ending index of subarray
#to print all possible subarrays
def print_all_subarrays(arr):
    n = len(arr)
    for start in range(n):
        for end in range(start, n):
            print(arr[start:end+1])

# kadane's algorithm

def max_subarray_sum(arr):
    max_ending_here = arr[0] # stores the sum of the current subarray you are building
    max_so_far = arr[0] # stores the best (maximum) sum seen so far

    # Traverse the array from the second element
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i]) # Update max_ending_here
        max_so_far = max(max_so_far, max_ending_here) # Update max_so_far if needed

    return max_so_far # Return the maximum subarray sum
# Example usage:
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(arr))  # Output: 6 (subarray [4,-1,2,1] has the largest sum)

'------------------------------------------------------------------------------'
'''10)Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the answer fits in a 32-bit integer.'''

def max_product_subarray(arr):
    n = len(arr)                         # Get the number of elements in the array

    if n == 0:                           # If the array is empty, return 0 (no product possible)
        return 0

    # Initialize tracking variables with the first element
    max_so_far = arr[0]                  # Maximum product ending at the current index
    min_so_far = arr[0]                  # Minimum product ending at the current index
    result = arr[0]                      # Global maximum product found so far

    # Traverse the array from the second element onward
    for i in range(1, n):
        # If current element is negative, swap max and min
        # because multiplying by a negative flips signs (handle negative numbers)
        if arr[i] < 0:
            max_so_far, min_so_far = min_so_far, max_so_far

        # Update max_so_far:
        # Either start a new subarray at arr[i], or extend the previous subarray
        max_so_far = max(arr[i], max_so_far * arr[i])

        # Update min_so_far:
        # Either start new at arr[i], or extend previous min product
        min_so_far = min(arr[i], min_so_far * arr[i])

        # Update global result if current max_so_far is larger
        result = max(result, max_so_far)

    # Return the highest product found among all subarrays
    return result

# Example usage:
arr = [-2, 6, -3, -10, 0, 2] # Output: 180
print(max_product_subarray(arr))  # Output: 180 (subarray [6, -3, -10] has the largest product) 

'''Example walk-through

Input: arr = [-2, 6, -3, -10, 0, 2]
Start: max_so_far = min_so_far = result = -2.

i=1 (6): positive → no swap.
max_so_far = max(6, -2*6) = max(6, -12) = 6
min_so_far = min(6, -2*6) = min(6, -12) = -12
result = max(-2, 6) = 6

i=2 (-3): negative → swap max_so_far & min_so_far (max_so_far=-12, min_so_far=6)
max_so_far = max(-3, -12 * -3) = max(-3, 36) = 36
min_so_far = min(-3, 6 * -3) = min(-3, -18) = -18
result = max(6, 36) = 36

i=3 (-10): negative → swap (max_so_far=-18, min_so_far=36)
max_so_far = max(-10, -18 * -10) = max(-10, 180) = 180
min_so_far = min(-10, 36 * -10) = min(-10, -360) = -360
result = max(36, 180) = 180

i=4 (0): zero → no swap
max_so_far = max(0, 180*0) = max(0, 0) = 0
min_so_far = min(0, -360*0) = min(0, 0) = 0
result = max(180, 0) = 180

i=5 (2):
max_so_far = max(2, 0*2) = 2
min_so_far = min(2, 0*2) = 0
result = max(180, 2) = 180

Final result is 180, coming from subarray [6, -3, -10] (6 × -3 × -10 = 180).'''

'-----------------------------------------------------------------------------------------'
'''11)You are given a circular array arr[] of integers, find the maximum possible sum of a non-empty subarray. In a circular array, the subarray can start at the end and wrap around to the beginning. 
Return the maximum non-empty subarray sum, considering both non-wrapping and wrapping cases.'''

def max_circular_subarray_sum(arr):
    def kadane(nums):
        max_ending_here = max_so_far = nums[0]
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    total_sum = sum(arr)
    max_kadane = kadane(arr)

    # Invert the array elements for finding the minimum subarray sum
    inverted_arr = [-x for x in arr]
    max_inverted_kadane = kadane(inverted_arr)
    min_subarray_sum = -max_inverted_kadane

    # If all numbers are negative, return the maximum element (max_kadane)
    if total_sum == min_subarray_sum:
        return max_kadane

    # Return the maximum of non-wrapping and wrapping cases
    return max(max_kadane, total_sum - min_subarray_sum)

# Example usage:
arr = [5, -2, 3, 4] # Output: 12
print(max_circular_subarray_sum(arr))  # Output: 12 (subarray [3, 4, 5] wraps around)

'''Short walk-through of the example arr = [5, -2, 3, 4]
total_sum = 5 + (-2) + 3 + 4 = 10

max_kadane (non-wrapping): Kadane on [5,-2,3,4] → best is 5 + (-2) + 3 + 4 = 10 (actually the whole array)
inverted_arr = [-5, 2, -3, -4]
Kadane on inverted gives max_inverted_kadane = 0? — let's compute properly:
running Kadane yields max = 2 (subarray [2]) → so max_inverted_kadane = 2
min_subarray_sum = -2 (minimum subarray in original is -2)

total_sum - min_subarray_sum = 10 - (-2) = 12 which corresponds to the wrapping subarray [3,4,5] (wraps around from end to start).

The function picks max(10, 12) = 12 → correct.
(Your printed example shows output 12, subarray [3, 4, 5]—that matches.)'''

'-----------------------------------------------------------------------------------'
'''You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.
Note: Positive number starts from 1. The array can have negative integers too.'''

def first_missing_positive(arr):
    n = len(arr)
    
    # Step 1: Clean the array by replacing non-positive numbers and numbers greater than n with n+1
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = n + 1
    
    # Step 2: Use the index as a hash to record the presence of numbers
    for i in range(n):
        num = abs(arr[i]) # Get the absolute value (in case it was marked negative)
        if 1 <= num <= n:
            arr[num - 1] = -abs(arr[num - 1]) # Mark the index as negative to indicate presence
    
    # Step 3: The first index which is positive indicates the missing number
    for i in range(n):
        if arr[i] > 0:
            return i + 1 # Return the first missing positive number
    
    return n + 1 # If all indices are marked, return n+1

# Example usage:
arr = [3, 4, -1, 1] # Output: 2
print(first_missing_positive(arr))  # Output: 2 (2 is the smallest missing positive number)

'----------------------------------OR----------------------------------'
def first_missing_positive(arr):
    n = len(arr)
    arr.sort() # Sort the array
    smallest_missing = 1 # Start checking from 1
    for i in range(0,n):
        if arr[i]==smallest_missing and arr[i]>=0: # If the current element matches the smallest missing positive
            smallest_missing+=1
    
    return smallest_missing
# Example usage:
arr = [3, 4, -1, 1] # Output: 2
print(first_missing_positive(arr))  # Output: 2 (2 is the smallest missing positive number)

'------------------------end----------------------------'
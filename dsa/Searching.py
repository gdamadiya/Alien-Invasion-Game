#SEARCHING
#Binary search says If you find your space min and mx, you can find your target in log(n) time. left right mid
#Linear search says You can find your target in O(n) time by checking each element one by one.
'''-------------------------------------------------------'''
'''1)Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[].'''

def count_occurrences(arr, target):
    def binary_search_left(arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search_right(arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    left_index = binary_search_left(arr, target)
    right_index = binary_search_right(arr, target)
    return right_index - left_index

# Example usage:
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(count_occurrences(arr, target))  # Output: 3

'''-------------------------or------------------------------'''
def count_occurrences_linear(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count
# Example usage:
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2  
print(count_occurrences_linear(arr, target))  # Output: 3

'''-------------------------------------------------------'''
'''2)A sorted array of distinct elements arr[] is rotated at some unknown point, the task is to find the minimum element in it.'''

class Solution:
    def findMin(self, arr):
        low, high = 0, len(arr) - 1
        while low < high: # binary search
            mid = (low + high) // 2
            if arr[mid] > arr[high]: # pivot is in the right half
                low = mid + 1 # move to the right half
            else: #arr[mid] <= arr[high]
                high = mid # move to the left half
        return arr[low]
# Example usage:
arr = [5, 6, 1, 2, 3, 4]
solution = Solution()
print(solution.findMin(arr))  # Output: 1
'''-------------------------or-----------------------------'''
def find_min_linear(arr):
    min_element = arr[0]
    for num in arr:
        if num < min_element:
            min_element = num
    return min_element
# Example usage:
arr = [5, 6, 1, 2, 3, 4]
print(find_min_linear(arr))  # Output: 1   
'''-------------------------------------------------------'''

'''3)Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key.  If the key is not present in the array, return -1.'''

class Solution:
    def search(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            if arr[low] <= arr[mid]: # left half is sorted
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else: # right half is sorted
                if arr[mid] < target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
# Example usage:
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0      
solution = Solution()
print(solution.search(arr, target))  # Output: 4
'''-------------------------or-----------------------------'''
def search_linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i    
    return -1
# Example usage:
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search_linear(arr, target))  # Output: 4   
'''-------------------------------------------------------'''

'''4)You are given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist).
If there are multiple peak elements, Return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".
Note: Consider the element before the first element and the element after the last element to be negative infinity.'''

class Solution:
    def peakElement(self, arr, n):
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
                return mid
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
# Example usage:
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)        
solution = Solution()
print(solution.peakElement(arr, n))  # Output: 2 (index of peak element 20)
'''-------------------------or-----------------------------'''
def peak_element_linear(arr):
    n = len(arr)
    for i in range(n):
        if (i == 0 or arr[i] >= arr[i - 1]) and (i == n - 1 or arr[i] >= arr[i + 1]):
            return i
        #arr[i] >= arr[i - 1]) Checks if the current element is greater than or equal to the previous element.
        #If i == 0 (first element), it doesn’t have a previous element, so we ignore that check.
    return -1
    #Why we are not using else The loop would stop at the first element because else executes immediately if the first element is not a peak.
    #You’d never check the rest of the array!

# Example usage:
arr = [1, 3, 20, 4, 1, 0]
print(peak_element_linear(arr))  # Output: 2 (index of peak element 20)

'''-------------------------------------------------------'''
# '''5)Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.'''
class Solution:
    def kthElement(self, a, b, k):
        a.extend(b)
        a.sort()
        k= k-1
        
        return a[k]
# Example usage:
a = [2, 3, 6, 7, 9] 
b = [1, 4, 8, 10]
k = 5
solution = Solution()
print(solution.kthElement(a, b, k))  # Output: 6

'''----------------------------------------------------------------------'''
'''6)You are given an array with unique elements of stalls[], which denote the positions of stalls. 
You are also given an integer k which denotes the number of aggressive cows. The task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.'''

class Solution:
    def canPlaceCows(self, stalls, k, distance):
        count = 1 # place the first cow in the first stall
        last_position = stalls[0] # position of the last placed cow
        for i in range(1, len(stalls)):
            if stalls[i] - last_position >= distance: # check if the current stall is at least 'distance' away from the last placed cow
                count += 1
                last_position = stalls[i]
                if count == k:
                    return True
        return False

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        low, high = 1, stalls[-1] - stalls[0]

        '''low = 1 → the minimum possible distance between two cows.
           high = stalls[-1] - stalls[0] → the maximum possible distance (between first and last stall).'''
        
        result = 0
        while low <= high: # binary search for the largest minimum distance
            mid = (low + high) // 2
            if self.canPlaceCows(stalls, k, mid): # can we place k cows with at least 'mid' distance apart?
                result = mid
                low = mid + 1 # try for a larger distance
            else:
                high = mid - 1
        return result
# Example usage:
stalls = [1, 2, 8, 4, 9]    
k = 3
solution = Solution()
print(solution.aggressiveCows(stalls, k))  # Output: 3

'''----------------------------------------------------------------------'''
'''7)Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

Each student receives atleast one book.
Each student is assigned a contiguous sequence of books.
No book is assigned to more than one student.
The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

Note: If it is not possible to allocate books to all students, return -1.'''

class Solution:
    # Helper function:
    # Checks if it is possible to allocate books to k students
    # so that no student reads more than maxAllowedPages.
    def isPossible(self, arr, n, k, maxAllowedPages): # n: number of books, k: number of students
        student_count = 1       # Start with the first student
        current_pages = 0       # Pages assigned to the current student

        for i in range(n):
            # If adding this book exceeds the allowed limit
            if current_pages + arr[i] > maxAllowedPages:
                student_count += 1         # Move to the next student
                current_pages = arr[i]     # Start counting for the new student
                
                # If more students are needed than available
                if student_count > k:
                    return False
            else:
                current_pages += arr[i]    # Assign book to current student

        return True  # Allocation possible within the given limit


    # Main function to find the minimum possible value of the maximum pages.
    def findPages(self, arr, n, k):
        # If there are fewer books than students, allocation not possible
        if n < k:
            return -1

        # Define the search range

        '''💡 Why low = max(arr) ?
Think about it:
Each student gets one or more books.
Books cannot be divided — each book must go fully to a single student.
Now, what’s the minimum possible “maximum pages per student”?
👉 It can’t be less than the largest book,
because someone has to read that book completely!'''

        low = max(arr)       # Lower bound: no student can take less than the largest book,startpoint
        high = sum(arr)      # Upper bound: one student takes all books, endpoint of array
        result = high        # Start with the maximum possible value

        # Binary search on the answer (minimize the maximum pages)
        while low <= high:
            mid = (low + high) // 2  # Candidate for the maximum pages

            if self.isPossible(arr, n, k, mid):
                result = mid      # Found a possible allocation
                high = mid - 1    # Try for a smaller maximum, moving left of array
            else:
                low = mid + 1     # Increase limit and try again, moving right of array

        return result
# Example usage:
arr = [12, 34, 67, 90]
n = len(arr)
k = 2
solution = Solution()
print(solution.findPages(arr, n, k))  # Output: 113
'''----------------------------------------------------------------------'''
'''8)Given a sorted array of distinct positive integers arr[], You need to find the kth positive number that is missing from the arr[].'''

def findKthPositive(arr, k):
    missing_count = 0
    current_number = 1
    index = 0

    while missing_count < k:
        if index < len(arr) and arr[index] == current_number:
            index += 1
        else:
            missing_count += 1
            if missing_count == k:
                return current_number
        current_number += 1

    return -1  # This line should never be reached if k is valid
# Example usage:
arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositive(arr, k))  # Output: 9
'''-----------------------OR--------------------------------'''

def findkthPositiveBinary(arr, k):
    i=1,j=0, count=0, n=len(arr)
    while count<k:
        if j < n and i==arr[j]:
            j+=1
            i+=1
        else:
            count+=1
            i+=1
    return i-1
    #When count == k, it means the previous number (i - 1) was the kth missing one.
# Example usage:
arr = [2, 3, 4, 7, 11]  
k = 5
print(findkthPositiveBinary(arr, k))  # Output: 9
'''--------------------------------------------------------'''

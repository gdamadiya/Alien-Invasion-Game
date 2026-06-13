#Shorting Algorithms

'''Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
Note: You need to solve this problem without utilizing the built-in sort function.'''

class Solution:
    def sort012(self, arr):
        count0 = 0
        count1 = 0
        count2 = 0
        
        for num in arr:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1
        
        index = 0
        
        for _ in range(count0): # Fill in 0s
            arr[index] = 0 # Fill in 0s
            index += 1
            
        for _ in range(count1): # Fill in 1s
            arr[index] = 1
            index += 1
            
        for _ in range(count2): # Fill in 2s
            arr[index] = 2
            index += 1
            
        return arr
    # Example usage:
solution = Solution()   
arr = [0, 1, 2, 0, 1, 2]
sorted_arr = solution.sort012(arr)
print(sorted_arr)

'''-------------------------------------------------------------------------------'''

'''2)You are given an array citations[], where each element citations[i] represents the number of citations received by the ith paper of a researcher. You have to calculate the researcher’s H-index.
The H-index is defined as the maximum value H, such that the researcher has published at least H papers, and all those papers have citation value greater than or equal to H.'''

class Solution:
    def hIndex(self, citations):
        n = len(citations)
        citations.sort(reverse=True)
        
        h_index = 0 # Initialize h_index to the maximum possible value (no of papers published -1(our index starts from 0))
        for i in range(n):
            if citations[i] >= i + 1: # Check if the citation count is greater than or equal to the current index
                h_index = i + 1 #
            else:
                break
                
        return h_index 
    # Example usage:
solution = Solution()
citations = [3, 0, 6, 1, 5]
h_index = solution.hIndex(citations)
print(h_index)

'''Explanation:
Sort descending → [6, 5, 3, 1, 0]

Check:
i = 0 → citations[0] = 6 ≥ 1 ✅
i = 1 → citations[1] = 5 ≥ 2 ✅
i = 2 → citations[2] = 3 ≥ 3 ✅
i = 3 → citations[3] = 1 ≥ 4 ❌ → stop '''

'''-----------------------------------------------------------------------------'''

'''3)Given an array of integers arr[]. You have to find the Inversion Count of the array. 
Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].'''

class Solution:
    def merge_and_count(self, left, right): # Merge two sorted arrays and count inversions
        i = j = 0
        merged = []
        inv_count = 0
        
        while i < len(left) and j < len(right): # Merge two sorted arrays and count inversions
            if left[i] <= right[j]:
                merged.append(left[i]) # Append smaller element
                i += 1
            else:
                merged.append(right[j]) # Append smaller element
                inv_count += len(left) - i # Count inversions
                j += 1
                
        merged.extend(left[i:]) # Append remaining elements
        merged.extend(right[j:])
        
        return merged, inv_count

    def merge_sort_and_count(self, arr):
        if len(arr) <= 1: # Base case
            return arr, 0
        
        mid = len(arr) // 2
        left, left_inv = self.merge_sort_and_count(arr[:mid]) #[left = [2,4,1], left_inv = 1], recursive call
    
        right, right_inv = self.merge_sort_and_count(arr[mid:]) #[right = [3,5], right_inv = 0], recursive call
        '''left = [2,4], left_inv = 0
           right = [1,3,5], right_inv = 0'''
        
        merged, merge_inv = self.merge_and_count(left, right)
        
        total_inv = left_inv + right_inv + merge_inv # Total inversions
        return merged, total_inv

    def inversionCount(self, arr): # Main function to count inversions
        _, inv_count = self.merge_sort_and_count(arr) #
        return inv_count
    # Example usage:
solution = Solution()
arr = [2, 4, 1, 3, 5]
inv_count = solution.inversionCount(arr)
print(inv_count)
'''Explanation:
                    [2, 4, 1, 3, 5]
                            |
             --------------------------------
             |                              |
         [2, 4, 1]                       [3, 5]
             |                              |
       -----------------               -------------
       |               |               |           |
     [2]           [4, 1]           [3]         [5]
                       |                            |
                 -------------                 (base cases)
                 |           |
               [4]         [1]
            (base cases)'''

'''----------------------------------------------------------------------------------------------'''

'''4)Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.'''

class Solution:
    def mergeIntervals(self, intervals):
        if not intervals: #check if the list is empty
            return []
        
        intervals.sort(key=lambda x: x[0]) # Sort intervals based on start time
        #x is each interval (like [1, 3], [2, 6], etc.)
        #x[0] means the start value of the interval.
        
        merged = [intervals[0]] # Initialize merged list with the first interval [importantmpoint]
        
        for current in intervals[1:]:
            last_merged = merged[-1] # Get the last merged interval
            
            if current[0] <= last_merged[1]: # Check for overlap
                last_merged[1] = max(last_merged[1], current[1]) # Merge intervals
            else:
                merged.append(current) # No overlap, add to merged list
                
        return merged
    # Example usage:
solution = Solution()
intervals = [[1, 3], [2, 4], [5, 7], [6, 8]]
merged_intervals = solution.mergeIntervals(intervals)
print(merged_intervals)
'''--------------------------------------------------------------------------------------'''
'''5)Geek has an array of non-overlapping intervals intervals[][] where intervals[i] = [starti , endi] represent the start and the end of the ith event and intervals is sorted in ascending order by starti . He wants to add a new interval newInterval[] = [newStart, newEnd] where newStart and newEnd represent the start and end of this interval.
Help Geek to insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).'''

class Solution:
    def insert(self, intervals, newInterval):
        merged = []
        i = 0
        n = len(intervals)
        
        # Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
            
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        merged.append(newInterval) # Add the merged newInterval
        
        # Add remaining intervals
        while i < n:
            merged.append(intervals[i])
            i += 1
            
        return merged
    # Example usage:
solution = Solution()
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
merged_intervals = solution.insert(intervals, newInterval)
print(merged_intervals)

'''--------------------------------------------------------------------------------------'''

'''6)Given a 2D array intervals[][], where intervals[i] = [starti, endi]. Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Note: Two intervals are considered non-overlapping if the end time of one interval is less than or equal to the start time of the next interval.'''

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1]) # Sort intervals based on end time
        
        count = 0
        end = intervals[0][1] # End time of the first interval
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < end: # Overlapping interval
                count += 1 # Increment count of intervals to remove
                end = min(end, intervals[i][1]) # Keep the interval with the earlier end time
            else:
                end = intervals[i][1] # Update end time
                
        return count
    # Example usage:
solution = Solution()
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
removed_intervals = solution.eraseOverlapIntervals(intervals)
print(removed_intervals)

'''--------------------------------------------------------------------------------------'''

'''7)Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space.
 Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.'''

class Solution:
    def merge(self, a, b):
        n = len(a)
        m = len(b)
        i = j = 0
        k = n - 1 # Pointer for the last element in a[](kwill move leftwards means right to left)

 #we are using while loop not for loop because we need to control i and k separately       
        while i <= k and j < m:
            if a[i] <= b[j]:
                i += 1
            else:
                a[k], b[j] = b[j], a[k] # Swap elements, remember we are swaping using k and j not i
                k -= 1
                j += 1
                
        a.sort() # Sort first array
        b.sort() # Sort second array
        
        return a, b
    # Example usage:
solution = Solution()
a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
merged_a, merged_b = solution.merge(a, b)
print("First array after merging:", merged_a)

'''Initial:

a = [1, 5, 9, 10, 15, 20] (n = 6)
b = [2, 3, 8, 13] (m = 4)
i = 0, j = 0, k = 5

Loop iterations (high level):
Compare a[0]=1 and b[0]=2: 1 <= 2 → i = 1.

Compare a[1]=5 and b[0]=2: 5 > 2 → swap a[5] and b[0]:
a becomes [1,5,9,10,15,2], b becomes [20,3,8,13]. Now k=4, j=1.

Compare a[1]=5 and b[1]=3: 5 > 3 → swap a[4] and b[1]:
a → [1,5,9,10,3,2], b → [20,15,8,13]. Now k=3, j=2.

Compare a[1]=5 and b[2]=8: 5 <= 8 → i=2.

Compare a[2]=9 and b[2]=8: 9 > 8 → swap a[3] and b[2]:
a → [1,5,9,8,3,2], b → [20,15,10,13]. Now k=2, j=3.

Now i=2 and k=2, compare a[2]=9 and b[3]=13: 9 <= 13 → i=3. Now i > k so loop stops.
After loop sorts:'''

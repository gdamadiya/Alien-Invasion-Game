##Hashing

'''1)Given an array arr[] of integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.'''

class Solution:
    def has_pair_with_sum(arr, target):
        seen = set() # To store the numbers we have seen so far
        for num in arr:
            complement = target - num # The number we need to find to form the target sum
            if complement in seen: #we are checking if the complement exists in the set
                return True
            seen.add(num)
        return False
# Example usage
arr = [10, 15, 3, 7]
target = 17 
print(Solution.has_pair_with_sum(arr, target))  # Output: True

'''2)You are given an array arr[] and an integer target. You have to count all pairs in the array such that their sum is equal to the given target.'''

class Solution:
    def count_pairs_with_sum(arr, target):
        count = 0
        freq = {}
        for num in arr:
            complement = target - num
            if complement in freq:
                count = count + freq[complement] #agar complement exist karta h to uski frequency jitni h utni baar count me add kar do.
            #adding new element in freq dictionary
            freq[num] = freq.get(num, 0) + 1 #jab new element aayega to uski frequency 1 ho jayegi aur agar pehle se exist karta h to uski frequency 1 se increment ho jayegi.
            #new element add karnge dict me (num,0) initially uska value 0 h.
        return count
# Example usage
arr = [1, 5, 7, -1, 5]
target = 6
print(Solution.count_pairs_with_sum(arr, target))  # Output: 3
'''--------------------------OR----------------------------------'''
    
class Solution:
    def countPairs(self, arr, target):
        n= len(arr)
        count=0
        
        for i in range(n):
            for j in range(i+1,n):
                if arr[i] + arr[j]== target:
                    count+=1
                    
        return count
# Example usage
arr = [1, 5, 7, -1, 5]  
target = 6
print(Solution.countPairs(arr, target))  # Output: 3

'''-------------------------------------------------------------'''
'''3)Given an array arr[], find all possible triplets i, j, k in the arr[] whose sum of elements is equals to zero. 
Returned triplet should also be internally sorted i.e. i<j<k.'''
#indices of triplets
class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        triplets = set()
        
        # Brute-force check of all combinations of (i, j, k)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] == 0:
                        triplets.add((i, j, k))
        
        # Convert to sorted list for consistent output
        result = sorted(list(triplets))
        return result
# Example usage
arr = [0, -1, 2, -3, 1]
print(Solution.findTriplets(arr))  # Output: [(0, 1, 4), (1, 2, 3)]
'''--------------------------------OR----------------------------'''
#values of triplets
class Solution:
    def findTriplets(self, arr, n):
        arr.sort()  # Sort the array first
        triplets = []  # Using a set to avoid duplicates

        for i in range(n):
            j, k = i + 1, n - 1 # Two pointers, j starts just after i, k starts at the end

            if i > 0 and arr[i] == arr[i - 1]: # Skip duplicate elements for i
                continue

            while j < k:
                current_sum = arr[i] + arr[j] + arr[k]

                if current_sum < 0: # If sum is less than zero, move the left pointer to the right
                    j += 1
                elif current_sum > 0:# If sum is greater than zero, move the right pointer to the left
                    k -= 1
                else:
                    # Add the triplet as a tuple (immutable, can go into a set)
                    triplets.add((arr[i], arr[j], arr[k]))
                    j += 1
                    k -= 1

                    while j < k and arr[j] == arr[j - 1]: # Skip duplicate elements for j
                        j += 1
                    while j < k and arr[k] == arr[k + 1]: # Skip duplicate elements for k
                        k -= 1

        # Convert set back to a list if needed
        return triplets
    
# Example usage
arr = [0, -1, 2, -3, 1] 
n = len(arr)
print(Solution.findTriplets(arr, n))  # Output: [(-3, 1, 2), (-1, 0, 1)]
'''-------------------------------------------------------------'''

'''4)Given two integer arrays a[] and b[], you have to find the intersection of the two arrays. Intersection of two arrays is said to be elements that are common in both the arrays. The intersection should not have duplicate elements and the result should contain items in any order.'''

class Solution:
    def intersection(self, a, b):
        set_a = set(a)  # Convert first array to a set to remove duplicates
        intersection_set = set()  # Set to store the intersection elements

        for element in b:
            if element in set_a:  # Check if the element from b is in set_a
                intersection_set.add(element)  # Add to intersection set

        return list(intersection_set)  # Convert the set back to a list before returning

# Example usage
a = [1, 2, 2, 1]    
b = [2, 2]
print(Solution().intersection(a, b))  # Output: [2]
'''-------------------------------------------------------------'''

'''5)You are given two arrays a[] and b[], return the Union of both the arrays in any order.
The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.'''

class Solution:
    def union(self, a, b):
        union_set = set(a)  # Start with all elements from the first array

        for element in b:
            union_set.add(element)  # Add elements from the second array

        return list(union_set)  # Convert the set back to a list before returning
    
# Example usage
a = [1, 2, 3]
b = [2, 3, 4]
print(Solution().union(a, b))  # Output: [1, 2, 3, 4]

'''-------------------------------------------------------------'''
'''6)Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.'''

class Solution:
    def findLongestConseqSubseq(self, arr, N):
        num_set = set(arr)  # Store all elements in a set for O(1) access
        longest_count = 0

        for num in arr:
            # Check if it's the start of a sequence
            if num - 1 not in num_set: #agar num-1 set me nahi h to iska matlab ye num sequence ka starting h.
                current_num = num # Initialize current number to the starting number
                current_count = 1

                # Count the length of the sequence
                while current_num + 1 in num_set: #jab tak current_num +1 set me h tab tak hum current_num ko increment karte jao aur current_count ko bhi increment karte jao.
                    current_num += 1
                    current_count += 1

                longest_streak = max(longest_streak, current_count)

        return longest_streak
    
'''------------------------------OR-------------------------------'''
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        n = len(arr)
        max_count=0
        count= 1
        for i in range(0,n):
            nums= arr[i]
            count= 1
            while nums + 1 in arr:
                count+=1
                nums+=1
            max_count= max(max_count, count)
        return max_count
    
# Example usage
arr = [100, 4, 200, 1, 3, 2]
n = len(arr)
print(Solution().findLongestConseqSubseq(arr, n))  # Output: 4

'''-------------------------------------------------------------'''
'''7)Given an array of strings, return all groups of strings that are anagrams. The strings in each group must be arranged in the order of their appearance in the original array. Refer to the sample case for clarification.'''

from collections import OrderedDict

class Solution:
    def anagrams(self, arr):
        anagram_map = OrderedDict()  # keeps insertion order of first appearance
        
        for word in arr:
            key = ''.join(sorted(word))  # sorted key for grouping
            
            if key not in anagram_map:
                anagram_map[key] = [] # word append karne se pehle key exist karta h ya nahi check kar lo nahi to loop fail hoga. nahi h to add key with empty list(value)
            anagram_map[key].append(word) # Append the word to the correct anagram group
        
        # Convert dictionary values to a list of groups
        return list(anagram_map.values())

# Example usage
arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().anagrams(arr))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

'''-------------------------------------------------------------'''

'''8)Given an unsorted array arr[] of integers, find the number of subarrays whose sum exactly equal to a given number k.'''
class Solution:
    def subarraySum(self, arr, k):
        n= len(arr)
        count=0
        for i in range(0,n):
            curr_sum=0       #initially curr_sum is 0, not a 1st element of your array.
            for j in range(i,n):
                curr_sum+= arr[j]
                if curr_sum== k:
                    count+=1

        return count
    
# Example usage
arr = [1, 1, 1]
k = 2
print(Solution().subarraySum(arr, k))  # Output: 2

'''------------------------------OR-------------------------------'''
class Solution:
    def countsubarrays(self, arr, k):
        prefixsum = {}
        result = 0
        current_sum = 0

        for num in arr:
            current_sum = current_sum + num # Update the current prefix sum

        # Check if the current prefix sum is equal to k

            if current_sum == k:
                result = result + 1
        # Check if there is a prefix sum that when subtracted from current_sum gives k

            if (current_sum - k) in prefixsum: #2-2=0 jo ki prefix sum me exist nahi karta h. {1:1} h 1st iteration me.
                result = result + prefixsum[current_sum - k] # Add the count of such prefix sums to the result

            prefixsum[current_sum] = prefixsum.get(current_sum, 0) + 1 # Update the frequency of the current prefix sum

        return result
    
# Example usage
arr = [1, 1, 1] 
k = 2
print(Solution().countsubarrays(arr, k))  # Output: 2

'''------------------------------OR-------------------------------'''

class Solution:
    def subarraySum(self, arr, k):
        count = 0
        curr_sum = 0
        sum_freq = {0: 1}  # Initialize with sum 0 occurring once

        for num in arr:
            curr_sum += num  # Update the current prefix sum

            # Check if there is a prefix sum that when subtracted from curr_sum gives k
            if (curr_sum - k) in sum_freq:
                count += sum_freq[curr_sum - k]

            # Update the frequency of the current prefix sum
            if curr_sum in sum_freq:
                sum_freq[curr_sum] += 1
            else:
                sum_freq[curr_sum] = 1

        return count

'''-------------------------------------------------------------'''

'''9)Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.'''

class Solution:
    def subarrayXor(self, arr, k):
        count = 0
        curr_xor = 0
        xor_freq = {0: 1}  # Initialize with XOR 0 occurring once

        for num in arr:
            curr_xor ^= num  # Update the current prefix XOR

            # Check if there is a prefix XOR that when XORed with curr_xor gives k
            if (curr_xor ^ k) in xor_freq:
                count += xor_freq[curr_xor ^ k]

            # Update the frequency of the current prefix XOR
            if curr_xor in xor_freq:
                xor_freq[curr_xor] += 1
            else:
                xor_freq[curr_xor] = 1

        return count
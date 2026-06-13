# Dynamic Programming
'''Longest Consecutive Subsequence ---> order doesn't matter
   Longest Increasing Subsequence (LIS) ---> order matter, We care about increasing order, not value consecutiveness'''


'''1)Given an array arr[] of non-negative integers, the task is to find the length of the Longest Strictly Increasing Subsequence (LIS).
A subsequence is strictly increasing if each element in the subsequence is strictly less than the next element.'''

def longest_increasing_subsequence(arr):
      n = len(arr)
      lis = [1] * n  # Initialize LIS values for all indexes as 1
   
      # Compute optimized LIS values in bottom up manner
      for i in range(1, n): # Outer loop → Runs once per index
         for j in range(0, i): # Inner loop → Checks ALL previous j's, but it's upto i-1 only.
               '''i loop runs once for i = 4
               j loop runs four times (j = 0,1,2,3) so wecompare arr[4] with arr[0], arr[1], arr[2], arr[3]'''
               
               if arr[i] > arr[j] and lis[i] < lis[j] + 1: # Only update if we found a better (longer) LIS
                  lis[i] = lis[j] + 1
   
      # Return maximum value in lis[]
      return max(lis)

# Example usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Length of Longest Increasing Subsequence is", longest_increasing_subsequence(arr))
# Output: Length of Longest Increasing Subsequence is 6

'''----------------------------------------------------------------------------'''

'''2)You are given an array of words where each word consists of lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB. For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k = 1.
Return the length of the longest possible word chain with words chosen from the given list of words in any order.'''
    

def longestStrChain(words):
    words.sort(key=len)  # Sort words by their lengths
    dp = {}  # Dictionary to store the longest chain ending with the word

    max_chain_length = 1  # Initialize maximum chain length

    for word in words:
        dp[word] = 1  # Each word is a chain of at least length 1
        # Try removing each character from the word to find its predecessor
        for i in range(len(word)):

            '''This removes the i-th character from the string using slicing.
            Remember: Strings are immutable in Python, so we can’t delete a character directly — instead, we create a new string without that character.'''

            predecessor = word[:i] + word[i+1:]  # Remove the i-th character, 0 se i-1 + i+1 se end tak, 1 rmove ho gya
            if predecessor in dp:
                dp[word] = max(dp[word], dp[predecessor] + 1)  # Update the chain length
        max_chain_length = max(max_chain_length, dp[word])  # Update global maximum

    return max_chain_length


# Example usage:
words = ["a","b","ba","bca","bda","bdca"]
print("Length of Longest String Chain is", longestStrChain(words))
# Output: Length of Longest String Chain is 4

'''----------------------------------------------------------------------------'''

'''3)Given two strings s1 and s2, return the length of their longest common subsequence (LCS). If there is no common subsequence, return 0.

A subsequence is a sequence that can be derived from the given string by deleting some or no elements without changing the order of the remaining elements. For example, "ABE" is a subsequence of "ABCDE".'''

def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)

    # dp[index1][index2], we used 0 to m and 0 to n to handle the base case of empty strings
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)] # Create a 2D array to store lengths of longest common subsequence, hack first use m (columns) inside list then n (rows),we added +1 to handle base case of empty strings
    #ek column and ek row extra add kiya h -1 python me last wala return karega to avaod that one java me it's ok.

    # Fill dp table
    for index1 in range(1, m + 1): # outer loop for s1
        for index2 in range(1, n + 1): # inner loop for s2

            # If characters match
            if s1[index1 - 1] == s2[index2 - 1]: # Match found, increment the count from previous indices
                dp[index1][index2] = dp[index1 - 1][index2 - 1] + 1 # Add 1 to the value from the previous indices

            # If characters don't match
            else:
                dp[index1][index2] = max(
                    dp[index1 - 1][index2],   # skip char from s1
                    dp[index1][index2 - 1]    # skip char from s2
                )

    return dp[m][n]  # The length of the longest common subsequence

# Example usage:
s1 = "AGGTAB"
s2 = "GXTXAYB"
print("Length of Longest Common Subsequence is", longest_common_subsequence(s1, s2))
# Output: Length of Longest Common Subsequence is 4
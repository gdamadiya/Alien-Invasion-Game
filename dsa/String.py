# String

'''1)Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

Cases for atoi() conversion:

Skip any leading whitespaces.
Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.'''

def myAtoi(s: str) -> int:      # Function to convert string to integer
    s = s.lstrip()              # 1️⃣ Remove leading whitespace characters
    if not s:                   # 2️⃣ If the string becomes empty after removing spaces
        return 0                #    → Return 0 immediately

    sign = 1                    # 3️⃣ Default sign is positive (+)
    if s[0] in ('-', '+'):      # 4️⃣ If the first character is a sign
        if s[0] == '-':         # 5️⃣ If it's a minus sign
            sign = -1           #    → Set sign to negative
        s = s[1:]               # 6️⃣ Remove that sign character from the string and update string.

    num = 0                     # 7️⃣ Initialize result number as 0
    for char in s:              # 8️⃣ Loop through each remaining character
        if char.isdigit():      # 9️⃣ If the character is a digit
            num = num * 10 + int(char)  # 🔟 Shift digits left and add new one
        else:                   # 11️⃣ If a non-digit is found
            break               #    → Stop parsing further

    num *= sign                 # 12️⃣ Apply the sign to the number

    INT_MAX, INT_MIN = 2**31 - 1, -2**31  # 13️⃣ Define 32-bit integer range

    if num < INT_MIN:           # 14️⃣ If number is smaller than minimum allowed
        return INT_MIN          #    → Clamp to INT_MIN
    if num > INT_MAX:           # 15️⃣ If number is greater than maximum allowed
        return INT_MAX          #    → Clamp to INT_MAX

    return num                  # 16️⃣ Return the final integer value
# Example usage:
# s = "   -42"  
# print(myAtoi(s))  # Output: -42

# Example usage:
s = "  -0012gfg4"
print(myAtoi(s))  # Output: -12

'-------------------Time Complexity: O(n)------------------'

'''2)Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.'''

def addBinary(s1: str, s2: str) -> str:
    i, j = len(s1) - 1, len(s2) - 1  # Pointers for s1 and s2 starting from the end means right side n-1 index
    carry = 0                        # Initialize carry to 0 
    result = []                      # List to store the result bits

    while i >= 0 or j >= 0 or carry: # Loop until both strings are processed and no carry remains
        bit1 = int(s1[i]) if i >= 0 else 0  # Get bit from s1 or 0 if index is out of range
        bit2 = int(s2[j]) if j >= 0 else 0  # Get bit from s2 or 0 if index is out of range

        total = bit1 + bit2 + carry         # Sum the bits and carry
        result_bit = total % 2               # Resulting bit is total mod 2
        carry = total // 2                    # Update carry for next iteration

        result.append(str(result_bit))       # Append the resulting bit to the result list

        i -= 1                               # Move to the next bit in s1
        j -= 1                               # Move to the next bit in s2

    final_result = ''.join(result).lstrip('0')   # remove leading zeros
    return final_result if final_result else '0' # Join the list into a string and return

# Example usage:
s1 = "00101"    
s2 = "0011"
print(addBinary(s1, s2))  # Output: "1000"
'-------------------Time Complexity: O(max(n, m))------------------'

'''3)Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.'''
#Anagram means same characters but in different order.

def areAnagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):          # 1️⃣ If lengths differ, they can't be anagrams
        return False                 #    → Return False immediately

    freq = [0] * 26                 # 2️⃣ Initialize frequency array for 26 letters

    for char in s1:                 # 3️⃣ Count frequency of each character in s1 ord gives ASCII value a=97,b=98...
        freq[ord(char) - ord('a')] += 1

    for char in s2:                 # 4️⃣ Decrease frequency based on characters in s2
        freq[ord(char) - ord('a')] -= 1
        if freq[ord(char) - ord('a')] < 0:  # 5️⃣ If any frequency goes negative
            return False             #    → s2 has extra characters not in s1

    return True                      # 6️⃣ If all frequencies are zero, they are anagrams
# Example usage:
s1 = "listen"   
s2 = "silent"
print(areAnagrams(s1, s2))  # Output: True
'-------------------Time Complexity: O(n)------------------'

def reverseWords(s: str) -> str:
    words = s.split()               # 1️⃣ Split the string into words (handles multiple spaces)
    reversed_words = words[::-1]    # 2️⃣ Reverse the list of words
    return ' '.join(reversed_words) # 3️⃣ Join the reversed words with a single space 
# Example usage:
s = "  Hello   World  "
print(reverseWords(s))  # Output: "World Hello"

'-------------------Time Complexity: O(n)------------------'

'''4)Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. 
If there is no non-repeating character, return '$'.'''

def firstNonRepeatingCharacter(s: str) -> str:
    freq = [0] * 26                 # 1️⃣ Initialize frequency array for 26 letters

    for char in s:                  # 2️⃣ Count frequency of each character in s
        freq[ord(char) - ord('a')] += 1

    for char in s:                  # 3️⃣ Find the first character with frequency 1
        if freq[ord(char) - ord('a')] == 1:
            return char             #    → Return that character immediately

    return '$'                      # 4️⃣ If no non-repeating character found, return '$'
# Example usage:
s = "leetcode"
print(firstNonRepeatingCharacter(s))  # Output: "l"
'-------------------Time Complexity: O(n)------------------'

'''5)Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. 
Use 0-based indexing while returning the indices.
Note: Return an empty list in case of no occurrences of pattern.'''

# KMP (Knuth–Morris–Pratt) Algorithm can be used to optimize the search to O(n + m) time complexity, but here is a simpler O(n*m) approach.

def searchPattern(txt: str, pat: str) -> list:
    result = []                     # 1️⃣ Initialize list to store starting indices of occurrences
    n, m = len(txt), len(pat)      # 2️⃣ Get lengths of text and pattern

    for i in range(n - m + 1):     # 3️⃣ Loop through text up to the point where pattern can fit
        if txt[i:i + m] == pat:    # 4️⃣ Check if substring matches the pattern if txt[0:0+3] == pat
            result.append(i)        #    → If match found, append starting index to result list

    return result                   # 5️⃣ Return the list of starting indices
# Example usage:
txt = "ababcabc"
pat = "abc"
print(searchPattern(txt, pat))  # Output: [2, 5]

''' range(n - m + 1) range(8-3+1)= range(6) instead of
range(n - m) = range(5) → [0, 1, 2, 3, 4]
That would miss the last possible start index (5),
where the substring "abc" actually appears in this example.

🔹 Visualization
r
Copy code
txt   =  a   b   a   b   c   a   b   c
index    0   1   2   3   4   5   6   7'''
'-------------------Time Complexity: O(n*m)------------------'

'''6)Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.
Note: A palindrome string is a sequence of characters that reads the same forward and backward.'''

def minCharsToPalindrome(s: str) -> int:
    def isPalindrome(sub: str) -> bool:  # Helper function to check if a string is palindrome
        return sub == sub[::-1]

    n = len(s)                          # Length of the original string

    for i in range(n, 0, -1):                  # Loop through each index, range(start, stop, step) reverse jayega agar n=3 to 3,2,1
        if isPalindrome(s[:i]):        # Check if the substring s[0:i] is a palindrome
            return n-i                 # Minimum characters to add is length of string - length of palindromic suffix  

    return n                            # If no palindrome found, return length of string

# Example usage:
s = "abc"
print(minCharsToPalindrome(s))  # Output: 2

#To find min chars to add in front, check longest palindromic prefix (not suffix). For min chars to add at end, check longest palindromic suffix.
#This function checks palindromic suffixes (s[i:]), so it returns minimum chars to add to the front or to the end?
'-------------------Time Complexity: O(n^2)------------------'

'''7)You are given two strings s1 and s2, of equal lengths. The task is to check if s2 is a rotated version of the string s1.
Note: A string is a rotation of another if it can be formed by moving characters from the start to the end (or vice versa) without rearranging them.'''

def isRotated(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):          # 1️⃣ If lengths differ, s2 can't be a rotation of s1
        return False                 #    → Return False immediately

    combined = s1 + s1              # 2️⃣ Concatenate s1 with itself eg: waterbottlewaterbottle

    return s2 in combined           # 3️⃣ Check if s2 is a substring of the concatenated string here we are checking erbottlewat in waterbottlewaterbottle

# Example usage:
s1 = "waterbottle" 
s2 = "erbottlewat"
print(isRotated(s1, s2))  # Output: True
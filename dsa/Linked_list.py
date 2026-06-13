##Linked list

'''1)You are given the head of a singly linked list. You have to reverse the linked list and return the head of the reversed list.'''

'''note-linked list means ek aisa data structure jisme elements sequentially connected hote hain through pointers. Har element ko node kehte hain, jisme do parts hote hain: ek data part aur ek pointer part jo agle node ko point karta hai.
head ka preious node null hota hai aur last node ka next pointer null hota hai, jo linked list ke end ko signify karta hai.'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr != None:
            next_temp = curr.next #store next node, because we are going to change curr.next to store addresh of next node.
            curr.next = prev # reverse the link (connection)
            prev = curr # move prev and curr one step forward
            # hum pehle prev ko curr pe set karte hain, phir curr ko next_temp pe set karte hain, order important hai
            curr = next_temp # move curr to next node
            
        return prev # prev will be the new head of the reversed list
    
# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)  
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
reversed_head = solution.reverseList(head)
# Function to print the linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
print_list(reversed_head)  # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
# Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once.
# Space Complexity: O(1), as we are using only a constant amount of extra space

'''2)You are given the head of a singly linked list, you have to left rotate the linked list k times. Return the head of the modified linked list.'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateLeft(self, head: ListNode, k: int) -> ListNode:
        # Step 1️⃣: Handle empty list or no rotation
        if not head or k == 0:
            return head

        # Step 2️⃣: Compute the length of the list
        length = 1
        curr = head
        while curr.next != None:
            curr = curr.next
            length += 1

        # Step 3️⃣: Normalize k (if k > length, only rotate k % length)
        k = k % length
        if k == 0:
            return head

        # Step 4️⃣: Move a pointer from head to find the (k-1)th node
        # This node will become the new tail after rotation.
        new_tail = head
        for _ in range(k - 1): #why k-1 we have started our len with 1 not 0.
            new_tail = new_tail.next

        # Step 5️⃣: The next node after new_tail becomes the new head
        new_head = new_tail.next

        # Step 6️⃣: Break the link — make new_tail the last node
        new_tail.next = None

        # Step 7️⃣: Traverse from new_head to the end (to get old tail)
        curr = new_head
        while curr.next:
            curr = curr.next

        # Step 8️⃣: Connect the old tail to the old head
        curr.next = head

        # Step 9️⃣: Return the new head
        return new_head
    
# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)  
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 2
solution = Solution()
rotated_head = solution.rotateLeft(head, k)
# Function to print the linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

print_list(rotated_head)  # Output: 3 -> 4 -> 5 -> 1 -> 2 -> None

'''------------------------------------------------------------------------------------'''
'''3)Given the head of two sorted linked lists consisting of nodes respectively. Merge both lists and return the head of the sorted merged list.'''
##Recursive method
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, head1: ListNode, head2: ListNode) -> ListNode:
        # Base cases
        if head1== None or head2== None:
            return head1 if head2== None else head2
             
        # Recursive case
        if head1.val <= head2.val: 
            '''yha head1 return karenge, next line me return head1 h uske next ko update kar rahe h phir se fun cl kar ke
               function ke under phir se head.next likha h jo current h, jo bahar h update new value se'''
            
            head1.next = self.mergeTwoLists(head1.next, head2) # linking the next of smaller node to the result of merging the rest
            return head1
        else:
            head2.next = self.mergeTwoLists(head1, head2.next)
            return head2
        
# Example usage:
# Creating first sorted linked list: 1 -> 3 -> 5    
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)
# Creating second sorted linked list: 2 -> 4 -> 6
list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)
solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)
# Function to print the linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
print_list(merged_head)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
# Time Complexity: O(n + m), where n and m are the lengths of the two linked lists.


'''------------------------------------------OR-------------------------------------------'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    '''1 -> 2 -> 4
    is represented as
    ListNode(1, ListNode(2, ListNode(4)))'''

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify the merging process
        dummy = ListNode()
        tail = dummy
        
        '''dummy → a temporary starting node (helps avoid special cases like empty lists)
            tail → points to the end of the merged list'''

        # Traverse both lists and append the smaller node to the merged list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # If there are remaining nodes in either list, append them
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # The merged list is next to the dummy node
        return dummy.next
    
# Example usage:
# Creating first sorted linked list: 1 -> 3 -> 5
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)
# Creating second sorted linked list: 2 -> 4 -> 6
list2 = ListNode(2) 
list2.next = ListNode(4)
list2.next.next = ListNode(6)
solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)
# Function to print the linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
print_list(merged_head)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
# Time Complexity: O(n + m), where n and m are the lengths of the two linked lists.
# Space Complexity: O(1), as we are merging the lists in place without using extra space.

'''------------------------------------------------------------------------------------'''
'''4)You are given the head of two singly linked lists head1 and head2 representing two non-negative integers. You have to return the head of the linked list representing the sum of these two numbers.'''

# Definition for a singly-linked list node
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data       # Store the digit value
        self.next = next       # Pointer to the next node


class Solution:
    # Helper function to reverse a linked list
    def reverse(self, head):
        prev = None
        while head:
            nxt = head.next    # Store next node
            head.next = prev   # Reverse the pointer
            prev = head        # Move 'prev' one step ahead
            head = nxt         # Move 'head' one step ahead
        return prev            # New head of the reversed list

    def addTwoLists(self, head1, head2):
        """
        Adds two numbers represented by linked lists (most significant digit first)
        and returns the sum as a new linked list.
        Example:
            Input: 7 -> 5 -> 9 (represents 759)
                   8 -> 4 -> 2 (represents 842)
            Output: 1 -> 6 -> 0 -> 1 (represents 1601)
        """

        # Step 1: Reverse both input lists to make addition easier (start from least significant digit)
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        # Step 2: Initialize a dummy node to build the result list
        dummy = ListNode()
        curr = dummy # dummy (0) after that it will add one by one addition but only one digit, second will carry
        carry = 0

        # Step 3: Traverse both lists until all digits and carry are processed
        while head1 or head2 or carry:
            # Get current digits from both lists (or 0 if list ended)
            x = head1.data if head1 else 0
            y = head2.data if head2 else 0

            # Calculate sum of digits + carry
            total = x + y + carry
            carry = total // 10                 # Carry for next iteration
            curr.next = ListNode(total % 10)    # Create new node with current digit
            curr = curr.next                    # Move to next position

            # Move ahead in both lists
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        # Step 4: Reverse the final result to restore original order (first is 0 which is dummy that what .next)
        return self.reverse(dummy.next)
    
    # Step 4: Remove leading zeros
        while result and result.data == 0 and result.next:
            result = result.next

        return result

# Example usage
# Helper function to create linked list from Python list
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" → " if head.next else "")
        head = head.next
    print()

head1 = create_linked_list([2, 4, 3])  # represents 342
head2 = create_linked_list([5, 6, 4])  # represents 465

print("Input List 1:")
print_linked_list(head1)

print("Input List 2:")
print_linked_list(head2)

# Call the solution
sol = Solution()
result = sol.addTwoNumbers(head1, head2)

print("\nOutput (Sum List):")
print_linked_list(result)

'''5)You are given the head of a singly linked list. You have to determine whether the given linked list contains a loop or not. A loop exists in a linked list if the next pointer of the last node points to any other node in the list (including itself), rather than being null.
Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null. Note that pos is not passed as a parameter.'''
#slow and fast approach

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def detectLoop(self, head):
        """
        Detects whether a loop exists in the linked list.

        Returns:
            True if a cycle/loop exists, False otherwise.
        """
        # 1) Start both pointers at the list head

        '''slow=0 we can't give like that 0 is integer and listnode is object type'''

        slow = head # initialize the slow pointer to point to the list’s head node. slow will move one step at a time
        fast = head # initialize the fast pointer to the same head node. fast will move two steps at a time

        # 2) Iterate while there are enough nodes ahead for 'fast' to move
        while fast != None and fast.next != None:
            # Move slow by one step
            slow = slow.next

            # Move fast by two steps
            fast = fast.next.next

            # 3) If they meet, there is a loop
            if slow == fast:
                return True

        # 4) If fast reached the end, there is no loop
        return False


# --------------------------
# Small test harness
# --------------------------
def build_list(values):
    """Helper to build a linked list from Python list and return head."""
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def print_result(has_loop):
    print("Loop detected." if has_loop else "No loop detected.")


# Example 1: No loop
head_no_loop = build_list([1, 2, 3, 4, 5])
sol = Solution()
print_result(sol.detectLoop(head_no_loop))  # Expected: No loop detected.

# Example 2: Create a loop (tail -> node at index 2; 1-based pos = 3)
head_loop = build_list([10, 20, 30, 40, 50])
# create loop: point last node (50) to the node with value 30
tail = head_loop
while tail.next:
    tail = tail.next
target = head_loop
for _ in range(2):  # move to 3rd node (0->10,1->20,2->30)
    target = target.next
tail.next = target  # make the loop

print_result(sol.detectLoop(head_loop))  # Expected: Loop detected.

''' finding starting starting node of linked list'''
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def detectLoopStart(self, head):
        """
        Detects if a loop exists and returns the starting node of the loop.
        If no loop, returns None.
        """

        # Step 1️⃣: Initialize both pointers
        slow = head
        fast = head

        # Step 2️⃣: Detect if a loop exists
        while fast != None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next

            # If both meet, a loop exists
            if slow == fast:
                break
        else:
            # If loop exits normally (no break), no loop found
            return None

        # Step 3️⃣: Find the starting point of the loop
        # Move one pointer to head, keep the other at meeting point
        fast = head

        # Move both pointers one step at a time until they meet again
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Both now point to the starting node of the loop
        return slow
    

    '''Remove node'''

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def removeLoop(self, head):
        """
        Detects and removes the loop in the linked list (if present).
        Modifies the list in-place.
        Returns True if a loop was found and removed, else False.
        """

        # Step 1️⃣: Use Floyd's Cycle Detection to check for a loop
        slow = head
        fast = head
        loop_exists = False

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:   # Loop detected
                loop_exists = True
                break

        # Step 2️⃣: If no loop, return False
        if not loop_exists:
            return False

        # Step 3️⃣: Find the starting node of the loop
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        # 'slow' (or 'fast') is now the start node of the loop
        loop_start = slow

        # Step 4️⃣: Find the last node in the loop (node whose next points to loop_start)
        ptr = loop_start
        while ptr.next != loop_start:
            ptr = ptr.next

        # Step 5️⃣: Break the loop
        ptr.next = None

        return True
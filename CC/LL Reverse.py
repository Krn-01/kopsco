class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse the
# linked list using a stack
def reverse_linked_list(head):
    # Create a temporary pointer
    # to traverse the linked list
    temp = head  
    
    # Create a stack to temporarily
    # store the data values
    stack = []   

    # Step 1: Push the values of the
    # linked list onto the stack
    while temp is not None:
        # Push the current node's
        # data onto the stack
        stack.append(temp.data) 
        # Move to the next node
        # in the linked list
        temp = temp.next        

    # Reset the temporary pointer
    # to the head of the linked list
    temp = head  

    # Step 2: Pop values from the stack
    # and update the linked list
    while temp is not None:
        
        # Set the current node's data to
        # the value at the top of the stack
        temp.data = stack.pop()  
        
         # Move to the next node in
         # the linked list
        temp = temp.next        

    # Return the new head of
    # the reversed linked list
    return head  

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)
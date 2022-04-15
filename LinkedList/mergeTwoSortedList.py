""" Python program to merge two
sorted linked lists """


# Linked List Node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create & Handle List operations
class LinkedList:

    def __init__(self):
        self.head = None

    # Method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    # Method to add element to list
    def addToList(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode


# Function to merge the lists
# Takes two lists which are sorted
# joins them to get a single sorted list
def mergeTwoList(list1, list2):
    # A dummy node to store the result
    dummy = LinkedList()
    # Tail stores the last node
    tail = dummy

    # Compare the data of the lists and whichever is smaller is
    # appended to the last of the merged list and the head is changed
    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        # Advance the tail
        tail = tail.next

    # If any of the list gets completely empty
    # directly join all the elements of the other list
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    # Returns the head of the merged list
    return dummy.next


# Create 2 lists
listA = LinkedList()
listB = LinkedList()

# Add elements to the list in sorted order
listA.addToList(5)
listA.addToList(10)
listA.addToList(15)

listB.addToList(2)
listB.addToList(3)
listB.addToList(20)

# Call the merge function
listA.head = mergeTwoList(listA.head, listB.head)

# Display merged list
print("Merged Linked List is:")
listA.printList()

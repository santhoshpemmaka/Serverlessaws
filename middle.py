# your task is to complete this function
# function should return index to the any valid peak element

# finding middle element in a linked list


def findMid(head):
  # Code here
    
  # firstly check the head is Nonereturn 0
    
  if head == None:
    return 0
  # In case first and second assign to the head of the linked list
  first = head
  second = head
  # checking  second and second next present in the linked list
  # If the logic useful to the linked list no the elements either even or odd numbers
  while second and second.next:
    first = first.next
    second = second.next.next
# return will be of the middle in the linked list
return first
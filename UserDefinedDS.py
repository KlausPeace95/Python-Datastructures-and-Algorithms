
# # LIST COMPREHENSION
# # Basic format: new_list = [transform sequence [filter]]
#
# import random
#
# under_50 = [x for x in range(50)]     # numbers from 0 to 49
# print('under_50: ' + str(under_50))
#
# # Get squared Numbers
# squares = [x**2 for x in under_50]
# print('Squares: ' + str(squares))
#
# # Get Odd Numbers
# odds = [x for x in range(50) if x%2 == 1]
# print('odds: ' + str(odds))
#
# # Get Multiples of 3
#
# mult_3 = [x for x in range(50) if x%3 == 0 and x > 0]
# print('Multiples of 3: ' + str(mult_3))
#
# # Strings
# s = 'My name is Klaus Peace, I am 27 years old and I understand 7 programming languages with 5 years experience'
# # Check Numeric values
# nums = [x for x in s if x.isnumeric()]
# print('Numbers: ' + ''.join(nums))
#
# # Get Index of a list item
# names = ['Brian', 'Joel', 'solange', 'Jude', 'Klaus', 'Joshua', 'James']
# idx = [k for k, v in enumerate(names) if v == 'Klaus']
# print('Index = ' + str(idx[0]))
#
# # delete item from a list
#
# letters = [x for x in 'ABCDEF']
# random.shuffle(letters)
# letter = [a for a in letters if a != 'C']
# print(letters, letter)


# STACKS QUEUES AND HEAPS

# STACKS (LIFO DS)
# push(), pop(), peek(), clear()
# Use Case: Commands Stack (Undo functions)
# Underlying datastructure of stack is a python list
my_stack = list()

# Pushing to stack using append
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print("Stack: ", my_stack)

print("Popping from Stack")
print("Stack", "after popping ", my_stack.pop(), ": ", my_stack)
print("Stack", "after popping ", my_stack.pop(), ": ", my_stack)
print("Stack", "after popping ", my_stack.pop(), ": ", my_stack, "\n")

# Stack using list with wrapper Class

print("Using my User-Defined Stack Function")

class Stack():
    def __init__(self):             # Constructor
        self.stack = list()         # Creates an empty list
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return "Underflow"
    def peek(self):                               # Looks at the top item in the stack without popping it off
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]  # Returns top item on the list without removing it.
        else:
            return None
    def __str__(self):                            # Shows all the items in the stack.
        return str(self.stack)

my_stack = Stack()

print("Pop from empty stack: ", my_stack.pop())
my_stack.push(8)
my_stack.push(0)
my_stack.push(34)
my_stack.push(45)
my_stack.push(11)

print("Stack: ", my_stack)
print("Popping ", my_stack.pop(), " Gives", my_stack)
print("Top Element of stack is: ", my_stack.peek())
print("All elements in stack are: ", my_stack.__str__())


# QUEUES  (FIFO DS)

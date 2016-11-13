# pop(items)
# pops an item from the stack passed in and returns it.
# Input: items, a stack
# Output: popped, the item popped from the stack or
#         "Empty Stack" if the stack was empty
def pop(items):
    size = len(items)
 
    if size > 0:
        popped = items[- 1]
        del(items[- 1])
        return popped
    else:
        return "Empty Stack"
 
 
# push(items, item)
# pushes the item passed in onto the stack passed in, items.
# Inputs: items, a stack
#         item,  an item to push onto the stack
# Output: None
def push(items, item):
    items.append(item)
 
     
def main():
    cars = []
    push(cars, 'Audi')
    print 'pushing Audi'
    push(cars, 'Buick')
    print 'pushing Buick'
    push(cars, 'Chevy')
    print 'pushing Chevy'
    push(cars,  'Dodge')
    print 'pushing Dodge'
    print
     
    while len(cars) > 0:
        print 'popping', pop(cars)
 
main()


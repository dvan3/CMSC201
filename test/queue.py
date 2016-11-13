#enqueue(q_items, item)
#adds an item passed in the queue, q_items
#Inputs:  q_items, a queue
#         item,    an item to add in the queue
#Outputs: None
def enqueue(q_items, item):

    #add the item into the queue, q_items
    q_items.append(item)

#dequeue(q_items)
#removes the first item that got added into the queue from the queue and
#returns it
#Inputs:  q_items, a queue
#Outputs: dequeued, the item that was removed from the queue.
def dequeue(q_items):

    #get the size of the queue
    size = len(q_items)

    #keep removing the first item in the queue from the queue until the
    #size of the queue is 0
    if size >  0:
        dequeued = q_items[0]
        q_items.remove(dequeued)
        return dequeued
    else:
        return "Empty queue"

def main():
    cars = []
    enqueue(cars, 'Audi')
    print 'enqueued Adui'
    enqueue(cars, 'Buick')
    print 'enqueued Buick'
    enqueue(cars, 'Chevy')
    print 'enqueued Chevy'
    enqueue(cars, 'Dodge')
    print 'enqueued Dodge'
    print

    while len(cars) > 0:
        print 'dequeuing', dequeue(cars)

main()

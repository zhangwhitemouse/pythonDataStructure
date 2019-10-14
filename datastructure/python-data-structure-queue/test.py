# from python_queue import Queue

# q = Queue()

# print(q.isempty())

# print(q.size())

# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)

# print(q.isempty())

# print(q.size())

# print("------------------")
# print(q.dequeue())
# print(q.dequeue())
# print("------------------")

# print(q.size())


from python_deque import Deque

deque = Deque()

print(deque.isempty())

print(deque.size())

deque.addfront(1)
deque.addfront(0)
deque.addrear(10)
deque.addrear(2)

print("----------------")

print(deque.isempty())

print(deque.size())

print("----------------")

print(deque.removefront())

print(deque.removerear())

print(deque.isempty())

print(deque.size())
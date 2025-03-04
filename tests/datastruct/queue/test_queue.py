from rcdsa.datastruct import ArrayQueue
from rcdsa.datastruct import LinkedQueue


def test_array_queue():
  n = 10
  q = ArrayQueue(n)
  for i in range(n):
    q.enqueue(i)
  while not q.is_empty():
    print(q.front(), end=" ")
    q.dequeue()

def test_linked_queue():
  n = 10
  q = LinkedQueue()
  for i in range(n):
    q.enqueue(i)
  while not q.is_empty():
    print(q.front(), end=" ")
    q.dequeue()
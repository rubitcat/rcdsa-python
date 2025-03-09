from rcdsa.datastruct import ArrayStack
from rcdsa.datastruct import LinkedStack


def test_array_stack():
  n = 10
  s = ArrayStack(n)
  for i in range(n):
    s.push(i)
  while not s.is_empty():
    print(s.top(), end=" ")
    s.pop()
  assert True

def test_linked_stack():
  n = 10
  s = LinkedStack()
  for i in range(n):
    s.push(i)
  while not s.is_empty():
    print(s.top(), end=" ")
    s.pop()
  assert True
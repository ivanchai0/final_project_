class _Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self._top = _Node(item, self._top)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека")
        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._top.value

    def is_empty(self):
        return self._top is None

    def size(self):
        return self._size
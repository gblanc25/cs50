class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, cookies):
        if self._size + cookies > self._capacity:
            raise ValueError("Too many cookies")
        self._size += cookies

    def withdraw(self, cookies):
        if self._size - cookies < 0:
            raise ValueError("Too few cookies")
        self._size -= cookies

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

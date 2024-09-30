class Entry:
    """
    Class: Entry
    Represents a key-value-priority tuple used in the priority queue.
    Methods:
    __init__(key, value, priority): Initializes an entry.
    __lt__(other): Compares priorities for heap operations.
    """
    def __init__(self, key, value, priority):
        self.key = key
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Entry(key={self.key}, value={self.value}, priority={self.priority})"


class LocatorBasedPriorityQueue:
    def __init__(self):
        self.heap = [None]  
        self.locator = {}

    def _swap(self, i, j):
        """Helper method to swap two elements in the heap and update their positions in the locator."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.locator[self.heap[i].key] = i
        self.locator[self.heap[j].key] = j

    def _bubble_up(self, index):
        """Maintain heap property by bubbling an entry up."""
        parent = index // 2
        while index > 1 and self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = index // 2

    def _bubble_down(self, index):
        """Maintain heap property by bubbling an entry down."""
        left = 2 * index
        right = 2 * index + 1
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self._swap(index, smallest)
            self._bubble_down(smallest)

    def put(self, entry):
        """Insert a new entry or update an existing one."""
        if entry.key in self.locator:
            index = self.locator[entry.key]
            self.heap[index].value = entry.value
            self.heap[index].priority = entry.priority
            self._bubble_up(index)
            self._bubble_down(index)
        else:
            self.heap.append(entry)
            index = len(self.heap) - 1
            self.locator[entry.key] = index
            self._bubble_up(index)

    def remove(self, key):
        """Remove an entry by key."""
        if key in self.locator:
            index = self.locator[key]
            self._swap(index, len(self.heap) - 1)
            self.heap.pop()
            del self.locator[key]
            if index < len(self.heap):
                self._bubble_up(index)
                self._bubble_down(index)

    def get(self, key):
        """Get an entry by key."""
        if key in self.locator:
            index = self.locator[key]
            return self.heap[index]
        return None

    def get_next(self):
        """Return the entry with the highest priority (root of the heap)."""
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def initialize(self, entries):
        """Initialize the heap with a list of entries."""
        self.heap = [None] + entries
        self.locator = {entry.key: i for i, entry in enumerate(self.heap) if entry}
        for i in range(len(self.heap) // 2, 0, -1):
            self._bubble_down(i)

    def get_all(self):
        """Return a copy of all entries. and Exclude the None at index 0"""
        return self.heap[1:]  

# Locator-Based Binary Heap Priority Queue

This project implements a **Locator-Based Binary Heap Priority Queue** in Python.

## Overview

A binary heap priority queue is a data structure that supports efficient insertion, deletion, and retrieval of the smallest (or largest) element in a collection. This implementation uses a **list** (array) and a **locator dictionary** to map keys to their positions in the heap for constant-time access.

## Data Structure

The priority queue is implemented using:
- A **Python list** (array) of `Entry` objects.
  - Each `Entry` has the following properties:
    - `key`: A unique identifier for the entry.
    - `value`: The value associated with the key.
    - `priority`: The priority of the entry (used to maintain heap order).
  - **Note**: The list uses index `0` as `None` to simplify the parent/child relationship in the heap.

- A **dictionary (locator)** that maps the `key` of an entry to its index in the list for O(1) access.

## Supported Methods

The class supports the following operations:

### `put(entry)` - O(log n) time
Inserts or updates an `entry` in the heap:
- If the key is already in the heap, the `put` method updates the `value` and `priority`, and reorders the heap (bubble/sift as needed).
- If the key isn't in the heap, the method adds the entry and maintains the heap property using **bubble up**.

### `remove(key)` - O(log n) time
Removes the entry with the given `key`:
- If the key is found, the entry is removed, and the heap is updated using **bubble up** or **bubble down** to maintain the heap property.

### `get(key)` - O(1) time
Returns a copy of the entry associated with the given `key`:
- The method retrieves the `Entry` object from the dictionary and returns its key, value, and priority.

### `get_next()` - O(1) time
Returns a copy of the root entry of the heap:
- This method returns the entry with the smallest (or largest) priority from the heap.

### `initialize(entries)` - O(n) time
Initializes the heap with a list of `entries`:
- This method clears the contents of the heap and adds the items listed in `entries`. It uses a **linear-time heapify** algorithm to ensure that the heap is constructed in O(n) time, rather than O(n log n).

### `get_all()` - O(n) time
Returns a copy of all the pending entries:
- This method returns a list of all the entries currently in the heap.

## Time Complexity

| Method       | Time Complexity |
|--------------|-----------------|
| `put(entry)` | O(log n)        |
| `remove(key)`| O(log n)        |
| `get(key)`   | O(1)            |
| `get_next()` | O(1)            |
| `initialize()`| O(n)           |
| `get_all()`  | O(n)            |


## Testing

Tests are written using `pytest`. To run the tests, use the following command:

```bash
pytest

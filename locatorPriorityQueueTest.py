import pytest
from locatorPriorityQueue import Entry, LocatorBasedPriorityQueue

def test_put():
    pq = LocatorBasedPriorityQueue()
    entry1 = Entry('a', 'task1', 1)
    entry2 = Entry('b', 'task2', 2)
    pq.put(entry1)
    pq.put(entry2)
    
    assert pq.get_next().key == 'a'  

def test_put_update():
    pq = LocatorBasedPriorityQueue()
    entry1 = Entry('a', 'task1', 1)
    entry2 = Entry('b', 'task2', 2)
    pq.put(entry1)
    pq.put(entry2)
    pq.put(Entry('a', 'task1_updated', 5))
    
    assert pq.get_next().key == 'b'  

def test_remove():
    pq = LocatorBasedPriorityQueue()
    entry1 = Entry('a', 'task1', 1)
    entry2 = Entry('b', 'task2', 2)
    entry3 = Entry('c', 'task3', 3)
    pq.put(entry1)
    pq.put(entry2)
    pq.put(entry3)
    pq.remove('a')  
    assert pq.get_next().key == 'b'  

def test_initialize():
    pq = LocatorBasedPriorityQueue()
    entries = [Entry('a', 'task1', 1), Entry('b', 'task2', 2), Entry('c', 'task3', 3)]
    pq.initialize(entries)
    assert pq.get_next().key == 'a'  

def test_get():
    pq = LocatorBasedPriorityQueue()
    entry1 = Entry('a', 'task1', 1)
    entry2 = Entry('b', 'task2', 2)
    pq.put(entry1)
    pq.put(entry2)
    assert pq.get('a').value == 'task1'
    assert pq.get('b').value == 'task2'
    assert pq.get('c') is None 

def test_get_all():
    pq = LocatorBasedPriorityQueue()
    entries = [Entry('a', 'task1', 1), Entry('b', 'task2', 2), Entry('c', 'task3', 3)]
    pq.initialize(entries)
    all_entries = pq.get_all()
    assert len(all_entries) == 3
    assert all(entry in all_entries for entry in entries)

def test_empty_heap():
    pq = LocatorBasedPriorityQueue()
    assert pq.get_next() is None
    assert pq.get('a') is None
    assert pq.get_all() == []

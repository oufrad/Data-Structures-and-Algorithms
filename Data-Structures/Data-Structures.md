# Arrays

Arrays, sometimes referred to as lists, organize items sequentially, one after another.

Arrays are the simplest and most commonly used data structure. They are ideal when you need to store data and iterate over it sequentially.

**Operations:**
- Lookup: O(1)
- Push: O(1)
- Insert: O(n)
- Delete: O(n)

## Static vs Dynamic Arrays

**Static Arrays:** 
Fixed in size, requiring the specification of the number of elements beforehand.

**Dynamic Arrays:**
Expand as new elements are added, so you don't need to specify the number of element when initializing it.

In dynamic arrays, adding an element might incur an O(n) time complexity because the array might need to be resized. However, some operations, such as pushing a new value, can be O(1).

In lower-level languages like C and C++, dynamic arrays require manual memory management using functions like `new` in C++ or `malloc` in C. Higher-level languages typically handle memory allocation automatically.

# Hash Tables

Hash tables, also known as hash maps, maps, unordered maps, or dictionaries, are fundamental data structures.

In programming languages like JavaScript, objects are a type of hash tables, while Python uses dictionaries, and Java offers Maps.

In contrast to arrays, where values are accessed via indices and stored sequentially in memory, hash tables utilize key-value pairs. A hash function maps each key to an address in memory, facilitating efficient storage and retrieval of values.

## What is a Hash Function?

A hash function generates a fixed-length value for each input it receives. Key attributes of a hash function include:

- It is a one-way function.
- It returns the same output for the same input.
- It produces different outputs for different inputs.

Hash tables offer fast access to data, making them invaluable in various data structures.

When storing key-value pairs in a hash table, the hash function determines where to store them in memory based on the generated hash.

## Hash Collisions

Hash tables exhibit the following time complexities:

- Insert: O(1)
- Lookup: O(1)
- Delete: O(1)
- Search: O(1)

While these complexities make hash tables highly efficient, hash collisions can occur. 

![Hash-Tables-Collisions](Hash-Tables-Collisions.png)

A **hash collision** arises when two elements share the same memory address. Although it's improbable for two keys to have identical hashed values, the memory address derived from the hash may not be unique due to its limited bit representation.

In the event of a collision, a linked list is formed, with the later-added element appended to the previously existing one.

Numerous methods exist to address hash collisions in hash tables.

To gain a better understanding of hash collision resolution, explore the visualization provided by [Open Hashing Visualization (usfca.edu)](https://www.cs.usfca.edu/~galles/visualization/OpenHash.html).
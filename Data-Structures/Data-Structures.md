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
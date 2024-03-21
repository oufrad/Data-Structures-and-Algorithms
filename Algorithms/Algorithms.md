## Recursion

Recursion, while not an algorithm itself, is a fundamental concept utilized in algorithm design.

**Recursion** involves a function calling itself within its definition.

It proves particularly effective for tasks featuring repeated subtasks.

Recursion is ubiquitous, appearing in various contexts such as:

- **DOM Traversal:** Navigating through the Document Object Model (DOM) of a web page often involves recursive operations.
  
- **Nested Objects:** In JavaScript, recursion is evident when dealing with objects containing nested objects.

Every recursive function must include a **base case** to halt the recursion. Failing to establish a base case can lead to the Stack Overflow Problem.

In recursion, both the base case and the recursive case must return values. The base case signals termination, while the recursive case propagates the desired result.

Recursion offers a powerful tool for solving problems with repetitive structures, providing elegant and concise solutions.

## 2. Sorting

Sorting might not be a primary concern when dealing with small datasets. However, the choice of sorting algorithm becomes critical when handling large volumes of data. Each problem requires a sorting method that best suits its characteristics. For instance, Google would employ its own sorting algorithms to arrange search results based on specific criteria, while Amazon and Netflix would utilize different algorithms for sorting products by categories or date.

One issue with the built-in sorting functionalities of most programming languages is their generic nature, which may not always align with your specific requirements.

While you may not typically implement your own sorting algorithms in your daily tasks, understanding how these algorithms work can greatly enhance your engineering skills. Familiarity with the trade-offs associated with each algorithm enables you to make informed decisions about when to use which sorting method.

### When to Use What ? 
Insertion sort is suitable for smaller sizes and nearly sorted data. However, bubble sort and selection sort are rarely used outside of educational contexts.

If you're concerned about worst-case scenarios, merge sort is a viable option. However, it consumes more space, so it may not be ideal if memory is limited.

In practice, merge sort and quick sort are among the most commonly used sorting algorithms due to their divide-and-conquer approach, which achieves O(n log(n)) performance.

### Comparison vs. Non-comparison Algorithms

All the algorithms discussed above are comparison algorithms (bubble sort, selection sort, insertion sort, merge sort, quick sort), which means they compare each element with another and adjust their order accordingly. The best time complexity achievable with these algorithms is O(n log(n)). However, there are non-comparison algorithms (such as radix sort and counting sort) that can guarantee much faster times, but they only work on lists of integers within a fixed range.

For more information on non-comparison algorithms:

- [Radix Sort | Brilliant Math & Science Wiki](https://brilliant.org/wiki/radix-sort/)
- [Counting Sort | Brilliant Math & Science Wiki](https://brilliant.org/wiki/counting-sort/)
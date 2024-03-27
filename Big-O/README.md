# Big O Notation
Big O notation is a fundamental concept in software engineering, crucial for understanding and analyzing the efficiency of algorithms. It is one of the most important concepts for programmers to grasp.

![Big-O-Notation-Graph](./imgs/Big-O-Notation.jpeg)

## 1. Understanding Big O Notation
Big O notation is used to classify algorithms based on how their runtime or space requirements grow relative to the size of their input.

* **O(1)**: Constant Time
* **O(n)**: Linear Time
* **O(n^2)**: Quadratic Time
* **O(n!)**: Factorial Time (the worst-case scenario)

## 2. Importance of Big O Notation
Imagine you build a function or program that executes quickly on your machine. However, a friend claims they've created a faster version. The relative performance of these functions may vary depending on the machine or context. Big O notation provides a standardized way to measure performance, focusing on the scalability of algorithms.

## 3. Calculating Big O Notation
Several rules guide the calculation of Big O notation:

**Worst Case:** Big O considers the worst-case scenario. For example, in a search algorithm, we consider the scenario where the target element is the last one encountered, requiring the algorithm to perform the maximum number of operations.

**Remove Constants:** Big O notation disregards constants, focusing on the overall growth rate of the algorithm. For instance, O(29129n + 82982) simplifies to O(n) because the linear growth dominates.

**Different Terms for Inputs:** Algorithms may have multiple input parameters, affecting their Big O notation. For example, a function operating on two lists has a notation of O(n + m), reflecting dependencies on both inputs.

**Drop Non-Dominants:** Only the most dominant term matters in Big O notation. For instance, O(n^2 + 6n + 500) simplifies to O(n^2) because, for large inputs, the quadratic term dominates.
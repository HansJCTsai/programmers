# Immigration (Binary Search)

Source: [Programmers - Immigration](https://school.programmers.co.kr/learn/courses/30/lessons/43238)

## Problem Description

There are **n** people waiting to pass immigration, and each officer takes a certain amount of time to process one person. Given an array `times`, where each element represents the time each officer takes to process a single person, we need to determine the **minimum time required for all people to be processed**.

### Constraints
- `1 ≤ n ≤ 1,000,000,000`
- `1 ≤ len(times) ≤ 100,000`
- `1 ≤ times[i] ≤ 1,000,000,000`

---

## Approach

This is a classic **minimization problem** that can be solved using **Binary Search**.

1. **Define search space**  
   - Minimum possible time = `1`
   - Maximum possible time = `max(times) * n` (the slowest officer processing everyone)

2. **Binary Search**  
   - For a candidate time `mid`, calculate how many people can be processed:  
     \[
     total = \sum_{i} \lfloor \frac{mid}{times[i]} \rfloor
     \]
   - If `total >= n`, it means `mid` minutes is enough → try to minimize further (search left half).  
   - Otherwise, increase time (search right half).

3. **Repeat** until `left > right`.  
   - The smallest feasible `mid` will be the answer.

---

# Stepping Stones (징검다리) — Programmers 43236

**Source**: https://programmers.co.kr/learn/courses/30/lessons/43236

## Problem
There is a destination located `distance` units away from the starting point. Between them, rocks are placed at various positions. You are allowed to remove some of these rocks.

For example, if the destination is 25 units away and the rocks are located at positions `[2, 14, 11, 21, 17]`, then after removing 2 rocks, the distances between the start, the remaining rocks, and the destination are as follows:

| Removed Rocks | Distances Between Points | Minimum Distance |
|---|---|---|
| [21, 17] | [2, 9, 3, 11] | 2 |
| [2, 21]  | [11, 3, 3, 8] | 3 |
| [2, 11]  | [14, 3, 4, 4] | 3 |
| [11, 21] | [2, 12, 3, 8] | 2 |
| [2, 14]  | [11, 6, 4, 4] | 4 |

Among the above, the largest minimum distance is **4**.

Given the total distance `distance`, an array `rocks` containing the positions of the rocks, and an integer `n` for the number of rocks to remove, write a function that returns the **maximum possible value of the minimum distance** between consecutive points (start, remaining rocks, and destination) after removing exactly `n` rocks.

## Constraints
- `1 ≤ distance ≤ 1,000,000,000`
- The number of rocks is between `1` and `50,000`, inclusive.
- `1 ≤ n ≤ number of rocks`

## I/O Example
| distance | rocks | n | return |
|---|---|---|---|
| 25 | [2, 14, 11, 21, 17] | 2 | 4 |

This matches the example above.

---

## Explanation
The task is to **maximize the minimum distance** between consecutive stepping stones when you can remove a given number of rocks.

If you try a greedy heuristic that repeatedly removes the rock that belongs to the **currently shortest gap**, you may fail to reach the optimal solution.

**Counterexample**

- Start / rocks / destination: `0, 7, 12, 15, 21, 33`
- Distances between rocks: `7, 5, 3, 6, 12`
- Number of rocks you may remove: `2`

**Greedy “remove shortest first” attempt**  
1) The shortest gap is `3`. Between its neighbors `5` and `6`, the left neighbor `5` is shorter, so remove the rock between `5` and `3` to merge them.  
   New gaps: `7, 8, 6, 12`  
2) The shortest gap is now `6`. Between its neighbors, the left neighbor `8` is shorter, so remove the rock between `8` and `6` to merge them.  
   New gaps: `7, 14, 12` → Minimum distance = `7`

However, the optimal choice at the start is to remove the rocks **between** `7` and `5`, and **between** `3` and `6`:
- New gaps: `12, 9, 12` → Minimum distance = `9` (better)

Therefore, the above heuristic does not work; we need another approach.

### Reverse View: “Given a target minimum distance, how many rocks must be removed?”
Consider flipping the perspective. Instead of asking “with `n` removals, what is the maximum minimum gap?”, ask:
> “To achieve a target minimum gap `X`, how many rocks must be removed?”

This can be determined **optimally** by a single pass:

**Example**  
- Gaps: `7, 5, 3, 6, 12`  
- Target minimum distance: `9`  

- `7 < 9` ⇒ merge with the next gap `5` → `(7+5) = 12 ≥ 9` → pass  
- `3 < 9` ⇒ merge with the next gap `6` → `(3+6) = 9 ≥ 9` → pass  
- `12 ≥ 9` → pass

We see that achieving a minimum distance of `9` necessarily requires removing **2** rocks.

Using this idea, we can define a feasible/infeasible check for any target `X` and then apply **binary search** over the answer range to find the largest feasible `X`.

---

## Tips (Binary Search Guardrails)
If the binary search termination condition is not set carefully, you can get stuck in an infinite loop in the final stage where `from` and `to` differ by 1.

**Example**
- Answer = `3`
- `from = 3`, `to = 4`
- `mid = (3 + 4) / 2 = 3`  
  The check passes for `mid = 3`, so you set `from = mid`, which remains `3`, and you loop forever.

To prevent this:
- Use `while (from + 1 < to)` as the loop condition, **or**
- Explicitly stop when `from + 1 == to` and then test `to`:
  - If feasible, choose `to`; otherwise choose `from`.

Either way, you avoid the off-by-one infinite loop at the end.

---

## Standard Approach (Outline)
1. Sort `rocks` ascending.
2. Binary search the answer `X` (minimum gap) over `[1, distance]`.
3. For each `X`, greedily scan from the start:
   - Maintain `prev` as the last kept point.
   - If `current - prev < X`, you must remove this rock; otherwise keep it and update `prev`.
   - After the loop, also check the final segment to the destination.
4. If the total removals `≤ n`, `X` is feasible; move right to try larger `X`. Otherwise move left.
5. Return the largest feasible `X`.
"""

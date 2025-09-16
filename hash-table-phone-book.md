## 📖 Problem: Phone Book

**Source:** [Programmers Problem 42577](https://programmers.co.kr/learn/courses/30/lessons/42577)

---

### Description

You are given a phone book containing several phone numbers. You need to check whether any number is a prefix of another number in the phone book.

For example, if the phone book contains the following numbers:

* Emergency services: `119`
* Junyoung Park: `97674223`
* Youngseok Ji: `1195524421`

Here, the emergency number `119` is a prefix of Youngseok Ji’s number `1195524421`.

Write a function `solution` that takes the array `phone_book` as input and returns **false** if there exists a number that is the prefix of another number. Otherwise, return **true**.

---

### Constraints

* `1 ≤ phone_book.length ≤ 1,000,000`
* `1 ≤ phone number length ≤ 20`

---

### Examples

| phone\_book                   | return |
| ----------------------------- | ------ |
| `[119, 97674223, 1195524421]` | false  |
| `[123, 456, 789]`             | true   |
| `[12, 123, 1235, 567, 88]`    | false  |

---

### Example Explanation

**Example 1**
As explained above, `119` is a prefix of `1195524421`.

**Example 2**
No number is a prefix of another, so the answer is `true`.

**Example 3**
The first number `"12"` is a prefix of the second number `"123"`. Therefore, the answer is `false`.

---

### Explanation

The problem asks whether any string in the given array is a prefix of another string. Although this problem is categorized under "Hash," it does not necessarily require hash tables to solve.

A brute-force approach would compare all pairs, which leads to **O(n²)** time complexity. To improve efficiency, note that only longer numbers can possibly have a shorter number as a prefix.

A common approach is:

1. Sort the phone numbers by length (or lexicographically).
2. For each number, compare it only against longer numbers, checking if the prefix matches.

---

### Tip

If you want to use hashing, you could override the `hashCode` method or define a custom class to ensure that comparisons only check the prefix length of the shorter string.

When comparing strings in Java, remember:

* Use `.equals()` to compare **content**.
* Don’t use `==`, since it only checks whether two variables refer to the same object in memory (like pointers in C).

---

Would you like me to also include a **clean Python solution with comments** at the end, so an American reader can immediately test the problem after reading the description?

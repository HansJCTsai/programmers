## 📌 Problem Description
[Programmers 42578 – Disguise](https://school.programmers.co.kr/learn/courses/30/lessons/42578)  

A spy must wear clothes every day. Clothes are divided into categories (e.g., hat, glasses, jacket), and each category may contain several items.  
The spy must wear **at least one item** each day.  

**Task:**  
Given a list of clothes, calculate the total number of distinct outfit combinations the spy can wear.  

---

## 🚀 Approach
1. Use a **Hash Table (dictionary in Python)** to count the number of items for each category.  
   - **Key:** category (e.g., headgear, eyewear)  
   - **Value:** number of items in that category  

2. For each category, the number of choices = `(count + 1)`  
   - The extra `+1` accounts for the option of **not wearing an item from that category**.  

3. Multiply the choices for all categories to get the total combinations.  

4. Subtract **1** at the end to remove the invalid case where the spy wears nothing at all.  

---

## 💻 Python Solution
```python
def solution(clothes):
    # Build a dictionary to count items by category
    clothes_map = {}

    for item, kind in clothes:
        clothes_map[kind] = clothes_map.get(kind, 0) + 1

    # Multiply (count + 1) for each category
    answer = 1
    for count in clothes_map.values():
        answer *= (count + 1)

    # Subtract 1 to exclude the "wear nothing" case
    return answer - 1

print(solution([
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"]
]))
# Output: 5
# headgear: 2 items → (2+1) = 3 choices
# eyewear: 1 item → (1+1) = 2 choices
# Total: 3 * 2 = 6, minus 1 = 5

print(solution([
    ["crow_mask", "face"],
    ["blue_sunglasses", "face"],
    ["smoky_makeup", "face"]
]))
# Output: 3
# face: 3 items → (3+1) = 4 choices
# Minus 1 = 3


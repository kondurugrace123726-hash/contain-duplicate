# Contains Duplicate (Python)
Efficient Python implementation to detect duplicate elements in an array using hash set for O(n) time complexity.

## 🧠 Problem Statement
Given an integer array, determine whether any value appears at least twice.  
Return 'True' if duplicates exist, otherwise return 'False'.

---
## 🚀 Approach
We use a **hash set** to track duplicate elements:

1. Traverse the array once
2. If element already exists in set → duplicate found
3. Otherwise, add it to the set

---

## ⏱ Complexity
- Time Complexity: **O(n)**
- Space Complexity: **O(n)**

"""
### 5. Remove Duplicates from List
**Question:**
Remove duplicate values while keeping order.

**Example Output:**
```text
Input: [1,2,2,3,4,4,5]
Output: [1,2,3,4,5]
```
"""


def remove_duplicates(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


def main():
    values = [1, 2, 2, 3, 4, 4, 5]
    unique_value = remove_duplicates(values)
    print(unique_value)


if __name__ == "__main__":
    main()

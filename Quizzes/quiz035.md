# Quiz035

## 1. Solution
```.py
def mystery(list1: list, list2: list) -> list:
    output = []
    for el1 in list1:
        for el2 in list2:
            if el1 == el2:
                output.append(el1)
                break

    return output
```

## 2. Proof of Work
![Quiz035](https://github.com/AntGra25/unit3-CS24/assets/142757981/288eb0e0-44fa-438c-a684-5b4ba4b5c49b)

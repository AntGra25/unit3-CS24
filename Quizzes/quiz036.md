# Quiz036

## 1. Solution
```.py
class Convert:
    def __init__(self):
        self.roman_symbols = {100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                              10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
                              }

    def convert_to_roman(self, decimal: int) -> str:
        output = ''
        if 0 < decimal < 101:
            for k, v in self.roman_symbols.items():
                q = decimal // k
                output += q * v
                decimal = decimal % k
        else:
            output = 'Invalid integer'

        return output
```

## 2. Proof of Work
![Quiz036](https://github.com/AntGra25/unit3-CS24/assets/142757981/dee1d4a7-25bc-4ce9-a204-e17de4f2d363)

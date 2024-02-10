Exercice 1: Manipulation de chaînes de caractères

1. 

```python
def reverse_string(s):
    return s[::-1]
```

2. 

```python
def capitalize_first_letter(s):
    return s[0].upper() + s[1:].lower()
```

3. 

```python
def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)
```

---

Exercice 2: Listes et tuples

1. 

```python
def common_elements(l1, l2):
    return [element for element in l1 if element in l2]
```

2. 

```python
def remove_duplicates(l):
    return list(set(l))
```

3. 

```python
def list_to_tuple(l):
    return tuple(l)
```

---

Exercice 3: Dictionnaires

1. 

```python
def word_count(s):
    words = s.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict
```

2. 

```python
def update_dictionary(d1, d2):
    for key, value in d2.items():
        if key in d1:
            d1[key] = value
        else:
            d1[key] = value
```

---

Exercice 4: Structures de contrôle

1. 

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

2. 

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

3. 

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

---

Exercice 5: Applications avancéesdef reverse_string(s: str):
    for i in enumerate(s):
        print(s[i])


reverse_string("Matthieu")


```python
def calculate_average(l):
    if not l:
        return None
    return sum(l) / len(l)
```

2. 

```python
def sort_list_of_tuples(l):
    return sorted(l, key=lambda x: x[0])
```

3. 

```python
def reverse_list(l):
    for i in range(len(l) // 2):
        l[i], l[-i - 1] = l[-i - 1], l[i]
```

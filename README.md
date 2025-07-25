# Mammadova_Python

This repository contains simple Python practice scripts written by Nuray Mammadova.

## ▶️ Tasks Included

### 🔹 task1.py
Checks if a number is greater than 7 and prints "Hello".

**Code Summary:**
```python
number = int(input("Enter a number:"))
if number > 7:
    print("Hello")
```

---

### 🔹 task2.py
Asks the user for a name. If the name is "John", it prints "Hello, John". Otherwise, it prints "There is no such name".

**Code Summary:**
```python
name = input("Enter a name:")
if name == "John":
    print("Hello, John")
else:
    print("There is no such name")
```

---

### 🔹 task3.py
Takes a list of numbers as input and prints only those that are divisible by 3.

**Code Summary:**
```python
numbers = [int(num) for num in input("Enter numbers separated by space: ").split()]

for num in numbers:
    if num % 3 == 0:
        print(num)
```

---

## 🛠 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/nuraymammadova7/Mammadova_Python.git
   ```

2. Navigate into the folder:
   ```bash
   cd Mammadova_Python
   ```

3. Run any script:
   ```bash
   python task1.py
   python task2.py
   python task3.py
   ```

---

## 🔗 Author

**Nuray Mammadova**  
GitHub: [nuraymammadova7](https://github.com/nuraymammadova7)

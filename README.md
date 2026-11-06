# Student Grade Manager

A simple command-line Python application to manage student records — add students, record their scores, calculate averages, and identify the top performer.

Built as a hands-on practice project applying core Python fundamentals: **dictionaries, functions, string formatting, and list operations**.

## Features

- **Add a student** — store a name along with a list of scores
- **View a student's average** — instant dictionary lookup, no searching needed
- **Find the topper** — automatically identifies the student with the highest average
- **View all students** — see every student's average, sorted alphabetically
- **Remove a student** — delete a record from the system

## How it works

Student data is stored in a dictionary, mapping each student's name to a list of their scores:

```python
students = {
    "Krishna": [67.0, 68.0, 69.0],
    "Arjun": [70.0, 98.0, 63.0]
}
```

Averages are calculated using Python's built-in `sum()` and `len()`:

```python
def get_average(name):
    scores = students[name]
    return sum(scores) / len(scores)
```

The topper is found using `max()` with a custom key function, so it compares students by their *calculated average* rather than by name or raw score list:

```python
topper = max(students, key=get_average)
```

## Running the project

```bash
python3 grade_manager.py
```

You'll see an interactive menu:

```
--- Student Grade Manager ---
1. Add Student
2. View Student Average
3. Find Topper
4. View All Students
5. Remove Student
6. Exit
Choose an option:
```

## Example session

```
Choose an option: 1
Enter student name: Krishna
Enter scores (space-separated): 67 68 69
Added Krishna with scores [67.0, 68.0, 69.0]

Choose an option: 2
Enter student name: Krishna
Krishna's average: 68.00
```

## What this project demonstrates

- Working with **dictionaries** as a key-value lookup structure
- Writing **functions with multiple parameters and return values**
- **String formatting** (f-strings, `.2f` precision)
- Basic **input validation** and error handling
- Building a simple **menu-driven CLI application**

## Author

Built as a practice project while preparing for software development internship applications.

"""
Student Grade Manager
----------------------
A simple command-line tool to add students, record their scores,
calculate averages, and find the topper.

Built using core Python fundamentals: dictionaries, functions,
string formatting, and list operations.
"""

students = {}


def add_student():
    """Add a new student along with their scores."""
    name = input("Enter student name: ").strip()
    raw_scores = input("Enter scores (space-separated): ").strip()

    try:
        scores = list(map(float, raw_scores.split()))
    except ValueError:
        print("Invalid scores entered. Please enter numbers only.")
        return

    if not scores:
        print("You must enter at least one score.")
        return

    students[name] = scores
    print(f"Added {name} with scores {scores}")


def get_average(name):
    """Return the average score for a given student."""
    scores = students[name]
    return sum(scores) / len(scores)


def view_average():
    """Print a specific student's average score."""
    name = input("Enter student name: ").strip()
    if name not in students:
        print(f"No record found for '{name}'.")
        return
    avg = get_average(name)
    print(f"{name}'s average: {avg:.2f}")


def find_topper():
    """Find and print the student with the highest average score."""
    if not students:
        print("No students added yet.")
        return
    topper = max(students, key=get_average)
    avg = get_average(topper)
    print(f"Topper: {topper} with average {avg:.2f}")


def view_all_students():
    """Print every student and their average score, sorted by name."""
    if not students:
        print("No students added yet.")
        return
    for name in sorted(students):
        avg = get_average(name)
        print(f"{name}: {avg:.2f}")


def remove_student():
    """Remove a student's record."""
    name = input("Enter student name to remove: ").strip()
    if name in students:
        del students[name]
        print(f"Removed {name}.")
    else:
        print(f"No record found for '{name}'.")


def menu():
    """Main interactive menu loop."""
    options = {
        "1": ("Add Student", add_student),
        "2": ("View Student Average", view_average),
        "3": ("Find Topper", find_topper),
        "4": ("View All Students", view_all_students),
        "5": ("Remove Student", remove_student),
        "6": ("Exit", None),
    }

    while True:
        print("\n--- Student Grade Manager ---")
        for key, (label, _) in options.items():
            print(f"{key}. {label}")

        choice = input("Choose an option: ").strip()

        if choice == "6":
            print("Goodbye!")
            break
        elif choice in options:
            _, action = options[choice]
            action()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()

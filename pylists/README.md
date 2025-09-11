# Python Lists Exercise

## Overview
This exercise focuses on **Python lists** and how to manipulate them interactively.  
Users can **check if an item exists in a list**, add new items, and practice basic list operations.

The main goals of this exercise are:
- Understand list creation and access.
- Practice `append()` to add new items.
- Use `in` to check if an item exists.
- Implement a simple interactive loop using `while`.
- Explore basic list methods and built-in functions.

---

## Files
- `animal_list.py` – main script for the exercise.

---

## How to Use

1. **Clone the repository** (if you haven't already):

```bash
git clone https://github.com/yourusername/your-repo.git
```
2. **Navigate to the exercise folder:**:

```bash
cd your-repo/exercise-animal-list
```
3. **Run the Python script**:

```bash
python animal_list.py
```

4. **Follow the prompts** to interact with the list of animals.
- Type the name of an animal to check if it is in the list.
- If the animal is not in the list, it will be automatically added.
- Type exit to quit the program.
_____

## Example Interaction

```Enter the name of an animal (or 'exit' to quit): dog
dog is already in the list
['dog', 'cat', 'elephant']

Enter the name of an animal (or 'exit' to quit): lion
lion is not in the list
Adding the animal to the list...
['dog', 'cat', 'elephant', 'lion']

Enter the name of an animal (or 'exit' to quit): exit
Exiting...
Program finished successfully!
```
______

## Useful List Methods

The script demonstrates or comments on the following list operations:

```Useful list methods
animal_list.append("new_animal")   # Add a new item
animal_list.pop()                  # Remove the last item
animal_list.pop(1)                 # Remove item at index 1
animal_list.remove("cat")          # Remove a specific item
len(animal_list)                   # Count the items in the list
sorted(animal_list)                # Return a sorted version of the list

```

**Other common operations you can explore:**

- sum(numbers) – sum all numbers in a list
- max(numbers) – maximum value
- min(numbers) – minimum value

_____

## Notes
- The program is case-insensitive when checking for the exit command (exit, Exit, EXIT all work).
- Designed for learning purposes, ideal for beginners practicing Python lists and loops.

## License
This project is free to use for learning purposes.

💼 **Connect with me:**

- GitHub: [https://github.com/joseamaury](https://github.com/joseamaury)  
- LinkedIn: [https://www.linkedin.com/in/jose-amaury-9910b6245/](https://www.linkedin.com/in/joseamaury/)  

✨ **Let's connect, collaborate, and code together!**  
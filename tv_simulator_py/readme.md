# Exercise: TV Class

This exercise is a practice of **Object-Oriented Programming (OOP)** in Python.  
The goal is to create a class that simulates the behavior of a television, allowing:

- Turn the TV on and off  
- Change channels up or down  
- Keep track of the current channel  

---

## Code

The code is in the `tv.py` file.

### Example of use:

```python
from tv import TV

# Create a TV
television = TV()

# Check if the TV is on
print(television.on)  # False

# Turn the TV on
television.power()
print(television.on)  # True

# Change channel
television.change_channel_up()
print(television.channel)  # 6

```
___

## Implementation details

The TV starts turned off (on = False) and on channel 5.

### Available methods:

```
power(): turns the TV on or off.

change_channel_up(): increases the channel (only if the TV is on).

change_channel_down(): decreases the channel (only if the TV is on).

```

The implementation ensures that channels only change when the TV is on.

___

## Author

**José Amaury**

[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/joseamaury)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joseamaury)
[![Gmail](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:amaury345.ja@gmail.com)

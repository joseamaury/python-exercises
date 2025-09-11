# List exercises in Python

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
animal_list = ["dog", "cat", "elephant"]
animal = str(())

while True:
    animal = input("Enter the name of an animal (or 'exit' to quit): ")
    if animal.lower() == "exit":
        print("Exiting...")
        break
    if animal in animal_list:
        print(animal, "is already in the list")
    else:
        print(animal, "is not in the list")
        print("Adding the animal to the list...")
        animal_list.append(animal)
    print(animal_list)

print("Program finished successfully!")

# Some useful list functions

# animal_list.pop()      # removes the last item in the list
# animal_list.pop(1)     # removes the item at index 1
# animal_list.remove("cat")  # removes the item "cat"
# print(sum(numbers))    # sums all numbers in the list
# print(max(numbers))    # maximum number in the list
# print(min(numbers))    # minimum number in the list
# print(len(numbers))    # number of items in the list
# print(sorted(numbers)) # returns a sorted version of the list

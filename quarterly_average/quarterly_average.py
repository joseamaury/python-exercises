a = int(input("First Term: "))
if a > 10:
    a = int(input("You entered the wrong grade. \nPlease enter the grade for the First Term again: "))
b = int(input("Second Term: "))
if b > 10:
    b = int(input("You entered the wrong grade. \nPlease enter the grade for the Second Term again: "))
c = int(input("Third Term: "))
if c > 10:
    c = int(input("You entered the wrong grade. \nPlease enter the grade for the Third Term again: "))
d = int(input("Fourth Term: "))
if d > 10:
    d = int(input("You entered the wrong grade. \nPlease enter the grade for the Fourth Term again: "))
average = (a+b+c+d) / 4
print("Your final grade is: {} ".format(average))
if average >= 7 and a <=10 and b <= 10 and c <=10 and d <= 10:
    print("Congratulations, you passed!")
elif average < 7:
    print("You have to take the remedial exam!")
else:
    print("An invalid grade was entered!")
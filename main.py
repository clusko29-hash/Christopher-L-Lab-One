name=input("What is your name? ")
print(name)
age=input("How old are you? ")
print(age)
color=input("What is your favorite color? ")
print(color)

age_num = int(age)
if age_num > 40:
    print("Hello ", name, "you are ", age, "your favorite color is", color, ". Are you sure u can use a computer?")
else:
    print("Hello ", name, "you are ", age, "your favorite color is", color, ".")
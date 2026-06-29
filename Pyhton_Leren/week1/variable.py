# Variable - A container for a value (string, integer, float, boolean, etc.) in Python.

#String Variable
first_name = "Yusuf" 
food = "pizza"
email = "yusuf@example.com"

print(first_name)  # Output: Yusuf 
print(f"hello {first_name}")  # Output: hello Yusuf
print(f"hello bro you like {food}") # Output: hello bro you like pizza
print(f"Your email is {email}")  # Output: Your email is yusuf@example.com

#Integer Variable
age = 25
quantity = 10
num_of_students = 30


print(f"your are {age} years old")  # Output: you are 25 years old
print(f"you are buying {quantity} items")  # Output: you are buying 10 items
print(f"there are {num_of_students} students in my class")  # Output: there are 30 students in my class

#Float Variable
price = 19.99
gpa = 3.5
distance = 5.2

print(f"the price is ${price} ")  # Output: the price is $19.99
print(f"your GPA is {gpa}") # Output : Your GPA is 3.5
print(f"you ran {distance} km")  # Output: you ran 5.2 km

#Boolean Variable
is_student = True
is_adult = False

print(f"are you a student? {is_student}")  # Output: are you a student? True
print(f"are you an adult? {is_adult}")  # Output: are you an adult? False 

if is_student:
    print("you are a successful student")  # Output: you are a successful student
else:
    print("you are not a student")  # Output: you are not a student



if is_adult:
    print("you are an adult")  # Output: you are an adult
else:
    print("you are not an adult")  # Output: you are not an adult
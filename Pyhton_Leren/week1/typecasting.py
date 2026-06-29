# typecasting = the procces of converting a variable from one data type to another 
# str() int() float() bool()

name = "Yusuf"  # string
age = 17 # integer
gpa = 3.5  # float
is_student = True  # boolean

print(type(name))  # Output: <class 'str'>
print(type(gpa))  # Output: <class 'float'>
print(type(age))  # Output: <class 'int'>
print(type(is_student))  # Output: <class 'bool'>

gpa = int(gpa)  # converting float to integer
print(gpa)

age =float(age)  # converting integer to float
print(age)

age = str(age)  # converting integer to string
print(age)
print(type(age))  # Output: <class 'str'>
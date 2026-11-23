# name = "Shawon Gazi"
# age = 23
# print("My name is", name, "My age is", age)
first_name = input("Enter your First Name :")
last_name = input("Enter your Last Name :")
age = input("Enter your Age :")
my_gf_name = input("Enter your Girlfriend Name :")

print(
    "My Name is "
    + first_name
    + " "
    + last_name
    + " and my age is "
    + age
    + " "
    + "and my girlfriend name is "
    + my_gf_name
)
# f-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces {}. They provide a more readable and concise way to format strings compared to traditional string concatenation or formatting methods.
print(
    f"My Name is {first_name} {last_name} and my age is {age} and my girlfriend name is {my_gf_name}"
)

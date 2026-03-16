name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

if age < 18:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print("\nHello", name)
print("You are categorized as:", category)
print("Your hobby is:", hobby)
# The app creates a pizza ordering App
print("Welcome to the Pizza Ordering App")
size = input("What pizza side do you want? S, M, L")
add_pepperoni = input("Do you want pepperoni?")
extra_cheese = input("Do you want extra cheese?")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill +=25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is{bill}")
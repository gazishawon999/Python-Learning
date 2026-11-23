# For loops :
for i in range(1, 6):  # This will print numbers from 1 to 5.
    print(i)  # Last number is not included in the range.

# for i in range(start, stop, step):

for i in range(1, 100, 1):
    if i % 2 == 0:
        print(i)

# Break statement in for loop:
for i in range(1, 51, 1):
    if i == 21:
        break
    if i % 3 == 0:
        print(i)
print("Out of loop")

# continue statement in for loop:
for i in range(1, 51, 1):
    if i == 21:
        continue
    if i % 3 == 0:
        print(i)
print("Out of loop")

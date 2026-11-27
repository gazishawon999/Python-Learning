def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    return c

if __name__ == "__main__":
    x = float(input("Enter 1st number: "))
    y = float(input("Enter 2nd number: "))
    z = float(input("Enter 3rd number: "))
    print(f"Largest: {largest(x, y, z)}")

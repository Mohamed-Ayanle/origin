# Define main
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# Define is_even
def is_even (n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
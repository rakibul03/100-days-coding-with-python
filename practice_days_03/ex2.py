n = int(input("Enter a number you want to multiply: "))

def mult(a):
    for b in range(1, 11):
        print(f"{a} x {b} = {a * b}")

mult(a = n)
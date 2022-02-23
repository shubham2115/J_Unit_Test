def conversion():  # function to convert celsius to Fahrenheit and vice versa
    print("1. Fahrenheit to celsius conversion")
    print("2. Celsius to Fahrenheit conversion")
    choice = int(input())
    if choice == 1:
        c = int(input("Enter value "))
        f = ((c * 9) / 5) + 32
        print(f"{c} celsius is {f} Fahrenheit")

    elif choice == 2:
        f1 = int(input("Enter value "))
        c1 = (f1 - 32) * 5 / 9
        print(f"{f1} fahrenheit is {c1} celsius")
    else:
        print("please select correct option")


conversion()

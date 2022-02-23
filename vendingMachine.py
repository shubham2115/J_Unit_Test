def notes():
    money = [1, 2, 5, 10, 50, 100, 200, 500, 2000]
    amount = int(input("Enter amount"))
    for i in range(1, 8):
        amount = amount / money[i]
    return amount


print(notes())

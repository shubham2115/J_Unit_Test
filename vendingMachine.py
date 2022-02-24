def count_currency(amount):
    notes = [2000, 500, 200, 100,
             50, 20, 10, 5, 1]

    print("****Currency Count****")

    for i in notes:
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print(i, " : ", j)


# Calling function
amount = int(input("Enter the amount :"))
count_currency(amount)

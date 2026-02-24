count = 0
while count <= 100:
    if count % 15 == 0:
        print("FIZZBUZZ")
    elif count % 3 == 0:
        print("FIZZ")
    elif count % 5 == 0:
        print("BUZZ")
    else:
        print(count)
    count += 1

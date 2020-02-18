import math

count = 0
try:
    digits = int(input("Enter number of Pi number digits: ")) + 1

    if digits == + 1:
        print("Empty sequence!")
    elif digits < + 1:
        print("Impossible to generate negative sequence")
    else:
        try:
            while count <= digits:
                print(str(math.pi)[count], end='')
                count += 1
        except IndexError:
            print("... To many digits")
except ValueError:
    print("Please, enter a valid number")

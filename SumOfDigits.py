
number = input("Please, enter 3 digits number: ")
if len(number) > 3:
    print("Enter 3 digits number next time!!!")
    quit()

result1 = int(number) % 10
result2 = int(number) // 10 % 10
result3 = int(number) // 100 % 10

print(result1+result2+result3)



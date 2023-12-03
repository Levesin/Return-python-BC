one = input("Запросил: ")
print(one)
print("-"*50)

two = one[1::2]

print(one)
print("Четные ->", two)

print("-"*50)
three = one[::-1]
print(three.upper())

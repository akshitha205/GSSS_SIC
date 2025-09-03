n = int(input("Enter the number: "))
digits = list(str(n))
length = len(digits)
found = False

for i in range(length - 2, -1, -1):
    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            digits[i], digits[j] = digits[j], digits[i] 
            found = True
            break
    if found:
        break

if found:
    print("The next possible bigger number is:", int(''.join(digits)))
else:
    print("Bigger number is not possible")
summ = 0

for number in range(1,1000000):
    if str(number) == str(number)[::-1]:
        if bin(number)[2:] == bin(number)[2:][::-1]:
            summ += number
print("Сумма палиндромов: " + str(summ))

summ = 0

for number in range(1, 1000):
    degree = number ** number
    summ = summ + degree
print (str(summ)[-10::]) 

import math 

fact = math.factorial
length = 20
weigth = 20
routes = fact(length + weigth) / (fact(length) * fact(weigth))

print(int(routes))

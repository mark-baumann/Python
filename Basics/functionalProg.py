x = lambda x: x * x
print(x(3))


#map
numbers = [x for x in range(10)]
squared = list(map(lambda x: x*2, numbers))
print(squared)



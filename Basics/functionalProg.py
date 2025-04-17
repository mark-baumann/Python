x = lambda x: x * x
print(x(3))


#map
numbers = [x for x in range(10)]
squared = list(map(lambda x: x*2, numbers))
print(squared)

#filter
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4]

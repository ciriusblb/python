demo_list = [1,'hello',1.34,True,[1,2,3]]
colors = ['red', 'blue', 'green']

numbers_list = list((1,2,3,4))
print(type(numbers_list))

r = list(range(1,101))
print(r)
print(len(colors))
print(colors[2])
colors.append('violet')
print(colors)
colors.extend(['black', 'white'])
print(colors)
colors.insert(-1,'pink')
print(colors)
colors.sort()
print(colors)
print(colors.count('red'))
#4.1 pizza

pizzas = ['peperoni', 'carbonara', 'mozarella']

for pizza in pizzas:
    print(f'I like {pizza.capitalize()} pizza.')
    
print(f'\nNice!')

for value in range(0,6):
    print(value)

print(f'\nNice!')

for value in range(6):
    print(value)
    
numbers = list(range(1,6))
print(*numbers, sep=", ")

even_numbers = list(range(0,11,2))
print(*even_numbers, sep=', ')

squares = []
for value in range(0, 12):
    squares.append(value**2)
print(*squares, sep=', ')
#same below
squares = [value**2 for value in range(0, 12)]
print(*squares, sep=', ')

#4.3

for number in range(0, 21):
    print(number, end=" ")
    
#4.4

spisok1 = list(range(1,1000001))
spisok2 = [num for num in range(1, 1000001)]
# if spisok1 == spisok2:
#     print(spisok1)

print(min(spisok1))
print(sum(spisok1))

odd_list = [num for num in range(1, 20, 2)]
print(*odd_list, sep=', ')

three_list = [num for num in range(3, 31, 3)]
print(*three_list, sep=', ')

cube_list = [num**3 for num in range(1, 11, 1)]
print(*cube_list, sep=', ')

#4.10

print(f'The first two items of the cube list are: {cube_list[:2]}')
print(f'The middle two items of the cube '
      f'list are: {cube_list[4:6]}')

print(f'The last two items of the cube list are: '
      f'{", ".join(map(str, cube_list[-2:]))}.')



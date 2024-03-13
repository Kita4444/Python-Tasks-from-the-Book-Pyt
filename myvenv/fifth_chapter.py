str1 = 'Stroka1'
str2 = 'StRoKa1'
print(str1 == str2)
print(str1.lower() == str2.lower())

alien_1 = {
    'color': 'green', 
    'y_position': 25, 
    'x_position': 0
    }
print(f"The alien is now {alien_1['color']}.")
# print(alien_1['points'])
del alien_1['y_position']
print(alien_1)

point_value = alien_1.get('points', 'No point value assigned.')
print(point_value)



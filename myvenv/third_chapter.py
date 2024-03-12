
# string formatting 

first_owned = 'bang'
four = 4
print(f"The first motorcycle I owned was a {first_owned.title()} and {4}.")

# invite friends to the party

friends_list = ['Kelen', 'Michael', 'Karina']
# for i in friends_list:
#     print(f'Hey, {i}! You have been invited to my birthday party! See you soon.')
    
# play around with the friend list

friends_list.pop()
print("Friend list:", ", ".join(friends_list) + ".")
friends_list = ['Kelen', 'Michael', 'Karina']
print("Friend list: " + ", ".join(friends_list) + ".")
del friends_list[0]
print("Friend list: " + ", ".join(friends_list) + ".")
friends_list.insert(1, 'Basil')
print("Friend list: " + ", ".join(friends_list) + ".")
friends_list.append('Kira')
print(*friends_list, sep=", ")
print("Friend list: " + ", ".join(friends_list) + ".")
# for i in friends_list:
#      print(f'Hey, {i}! You have been invited to my birthday party! See you soon.')

#3.7 
while len(friends_list) > 2:
    i = 0
    print(f'Hey, {friends_list[len(friends_list) - 1 - i]}! Sorry, I cannot invite you to my party...')
    friends_list.pop()
    i += 1
print("Friend list: " + ", ".join(friends_list) + ".")

del friends_list[1]
del friends_list[0]
print("Friend list: " + ", ".join(friends_list) + ".")

#3.8

print(f'\n\nThis is the new task:\n\n')
countries = ['Italy', 'Germany', 'China', 'Netherlands', 'Austria']
countries.reverse()
print(countries)
countries.reverse()
print(countries)
print(sorted(countries))
print(countries)
print(sorted(countries, reverse=True))
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)


    
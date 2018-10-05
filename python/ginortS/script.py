inpt = input()
sorted_string = []
sorted_string.extend(sorted([character for character in inpt if character.islower()]))
sorted_string.extend(sorted([character for character in inpt if character.isupper()]))
sorted_string.extend(sorted([character for character in inpt if character.isdigit() and int(character)%2 is 1]))
sorted_string.extend(sorted([character for character in inpt if character.isdigit() and int(character)%2 is 0]))
print(''.join(sorted_string))
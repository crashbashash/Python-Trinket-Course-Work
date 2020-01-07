first_name = input('Enter first name: ')
middle_name = input('\nEnter middle name: ')
surname = input('\nEnter surname: ')

if middle_name.strip() != "":
  print('{0}, {1}.{2}.'.format(surname.capitalize(), first_name[0].capitalize(), surname[0].capitalize()))
else:
  print('{0}, {1}'.format(surname.capitalize(), first_name.capitalize()))

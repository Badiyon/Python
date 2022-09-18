title = 'days of the week\n'
path = '/users/badiy/desktop/days.txt'
days_file = open(path, 'r')
days = days_file.read()

new_path = '/users/badiy/desktop/new_days.txt'
new_days = open(new_path, 'w')

new_days.write(title)
print(title)

new_days.write(days)
print(days)
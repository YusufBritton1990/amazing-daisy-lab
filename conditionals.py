name = "Adam"
tired = False

if name == "Adam" and not tired:
    print("Adam is not tired")
else:
    print('Something is not right');

age = 39
ticket = 'child' if age < 13 else 'adult'

if age < 13:
    ticket = 'child'
else:
    ticket = 'adult'

print(ticket)
def make_pizza(size, stuff_crust = False, cheese_type ='mozzarella', sauce_type = 'tomato'):
    if stuff_crust:
        print(f'Your {size} inch stuff crust pizza with {cheese_type} cheese '
              f'and {sauce_type} sauce will be ready soon')
    else:
        print(f'Your {size} inch pizza with {cheese_type} cheese '
              f'and {sauce_type} sauce will be ready soon!')

# make_pizza(16)
# make_pizza(16, True)
# make_pizza(16, True, 'cheddar')

# make_pizza(16,sauce_type='BBQ')

def build_info(name, height, number = 111):
    return f'My name is {name}, I am {height} inches tall, and my favorite number is {number}'

# result = build_info('Fred', 68,256)
# print(result)
#
# result2 = build_info(name = 'Sally', height = 66, number = 1000)
# print(result2)
#
# result3 = build_info(height = 70, number = 12345, name = 'Carlos')
# print(result3)
#
# result4 = build_info('Bob', number=123)
# print(result4)

# make_pizza(10, True, sauce_type = 'pesto')
# this = 1
# that = 1
#
# if this:
#     print('then that')
#
# elif that:
#     print('then this')
#
# for x in range(0,8):
#     print(x)
#
# def this_funct(a,b,c):
#     pass

def add_one(x):
    return x + 1

result1 = add_one(10)
print(result1)

add_one_again = lambda x: x + 1

result2 = add_one_again(10)
print(result2)


def will_it_rain:
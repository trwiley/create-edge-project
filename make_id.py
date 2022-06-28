import random
hex = '0123456789abcdef'
id = ''.join([random.choice(hex) for x in range(32)])

print(id)
import random
import string
chars = string.ascii_letters + string.digits + string.punctuation
length = int(input("Length: "))
password = ''.join(random.choice(chars) for _ in range(length))
print("Password:", password)

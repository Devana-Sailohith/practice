import random
import string

randomFirstName = random.randint(5, 8)
random_strf = ''.join(random.choices(string.ascii_letters, k=randomFirstName))
randomLastName = random.randint(5, 8)
random_strl = ''.join(random.choices(string.ascii_letters, k=randomLastName))
print(random_strf+random_strl+"@gmail.com")

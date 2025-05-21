import random
import string

class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length

    def generate_password(self):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(self.length))
        password_list = list(password)
        random.shuffle(password_list)
        return ''.join(password_list)

    def display(self):
        password = self.generate_password()
        print(f"Generated Password: {password}")

pgen = PasswordGenerator(14)
pgen.display()
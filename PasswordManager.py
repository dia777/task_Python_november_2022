from Singleton import SingletonMeta
import random


class PasswordManager(metaclass=SingletonMeta):
    def write_password(self, account):
        password = self.generate_password()
        with open('mi_fichero(2).txt', 'a') as f:
            f.write(account + ' ')
            f.write( password + '\n')
        return password
    
    def read_password(self, account):
        password = ''
        with open('mi_fichero(2).txt', 'r') as f:
            for line in f:
                line = line.rstrip()
                text =line.split(' ')
                name = text[0]
                password = text[1]
                if account == name:
                    return password
        return 'Password not found'



    def generate_password(self):
        capital_letters = ['A' , 'B', 'C' , 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lower_letters = ['a' , 'b', 'c' , 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        all = capital_letters + lower_letters + numbers
        password = []
        for i in range(1,random.randint(9,16)):
            character_random = random.choice(all)
            password.append(character_random)
        
        password = "".join(password)
        return password
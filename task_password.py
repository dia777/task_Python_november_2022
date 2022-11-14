import random

mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minus = "abcdefghijklmnñopqrstuvwxyz"
num = "0123456789"

all=mayus+minus+num

for i in range (1,random.randint(9,16)):
    character_randon = random.choice(all)
    print(character_randon)
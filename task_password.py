import random

def generate_password():
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

get_process = '0'
psdword_dic = {}

while get_process != '3':
   print("1. Generate Password")
   print("2. Get Password")
   print("3. Exit")
   get_process = input("SELECT A NUMBER")
   if get_process =='1':
    account = input('ENTER YOUR ACCOUNT NAME:') 
    psdword_dic[ account ] = generate_password()
    print("\n", account, ":", psdword_dic[account])

   elif get_process == '2':
        account = input("ENTER THE NAME OF THE ACCOUNT FOR WHICH YOU WANT TO GET THE PASSWORD FOR")
        if account in psdword_dic:
           print("\n", account, ":", psdword_dic[account])
        else:
            print("No exit")
   elif get_process == '3':
      print("GOODBYE")
       #pass
   else:
      print("THE NUMBER YOU ENTERED IS NOT CORRECT") 
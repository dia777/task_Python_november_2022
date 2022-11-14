from PasswordManager import PasswordManager   
get_process = '0'
psdword_dic = {}

while get_process != '3':
   print("1. Generate Password")
   print("2. Get Password")
   print("3. Exit")
   get_process = input("SELECT A NUMBER")
   if get_process =='1':
    account = input('ENTER YOUR ACCOUNT NAME:') 
    psdword_dic[ account ] = PasswordManager().write_password(account)
    print("\n", account, ":", psdword_dic[account])
   elif get_process == '2':
        account = input("ENTER THE NAME OF THE ACCOUNT FOR WHICH YOU WANT TO GET THE PASSWORD FOR")
        password = PasswordManager().read_password(account)
        print(password)
   elif get_process == '3':
      print("GOODBYE")
       #pass
   else:
      print("THE NUMBER YOU ENTERED IS NOT CORRECT")  


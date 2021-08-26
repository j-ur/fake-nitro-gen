
import random, string
import webbrowser

print("Discord Nitro Gen")
print("council#0482 @ discord")


num=input('Number of nitros: ')

f=open("Codes.txt","w", encoding='utf-8')

print("Generating..")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()
input("\n\nCodes printed in Codes.txt")

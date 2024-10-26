
import random

'''
-1 Siccore
 1 Rock
 0 Paper

 
Scissors cuts Paper (Scissor wins over Paper)
Rock blunts Scissors (Rock wins over Scissors)
Paper covers Rock (Paper wins over Rock)

'''

computer =random.choice([-1,0,1])
youcheck=input(f"\nEnter r-p-s for playing Rock-paper-scissor : ")


reverse={'r':1,'p':0,'s':-1}
you=reverse[youcheck]

comp={1:'rock',0:'paper',-1:'scissor'}

print(f"\nYou have entered : {comp[you]} \ncomputer has entered : {comp[computer]}\n")

if(computer==you):print(f"Its Draw!\n")

if((computer ==0 and you==-1) or (computer ==-1 and you==1) or (computer ==1 and you==0)):print(f"You wins!\n")
else:print(f"Compuer Wins!\n")
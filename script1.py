# # print("Welcome to the tip calculator!")
# # Total_Bill =float( input("what was the total bill?"))
# # tip =float(input("How much tip would you like to give? 10 ,12  or 15?"))
# # No_Of_People= int(input("How many people to split the bill?"))
# #
# #
# # tip_amount= Total_Bill*(tip/100)
# # final_bill=Total_Bill+tip_amount
# # per_person= final_bill/No_Of_People
# #
# #
# # print(f"Each person should pay: {per_person:.2f}")
# #
#
#
# number =int(input("Enter a number to check whetehr it is even or odd \n"))
# if number %2==0:
#     print(f"number {number} is even")
# else:
#     print(f"number {number} is odd")
#

# print("welcome to python pizza deliveries")
# size=input("What size pizza do you want? S,M or L:")
# pepporoni=input("Do you want pepperoni on your pizza? Y or N:")
# extra_cheese =input("Do you want extra cheese? Y or N:")
#
# bill =0;
#
#
# if size =="S":
#     bill=bill+15
# elif size== 'M':
#     bill=bill+20
# elif size =="L":
#     bill=bill+25
# else:
#     print("Wrong inputs")
# if pepporoni =="Y":
#        if size =="S":
#            bill=bill+2
#        else:
#            bill=bill+3
# if extra_cheese =="Y":
#     bill=bill+1
#
#     print(f"Your final bill is: ${bill}")



import random

# random_integer =random.uniform(1,10)
# print(random_integer)

#
#
# random_heads_or_tails=random.randint(0,1)
# print(random_heads_or_tails)
# if random_heads_or_tails ==1:
#  print("heads")
# else:
#  print("tails")
#
#
#
#  frinds= ["Amber","jayant","Suraj"]
#  print(random.choice(frinds))



# Rock Paper Scissors ASCII Art

# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")



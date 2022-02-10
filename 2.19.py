#Johnny La
#PSID: 1875393

lemon=float(input("Enter amount of lemon juice (in cups):\n"))
water=float(input("Enter amount of water (in cups):\n"))
agave=float(input("Enter amount of agave nectar (in cups):\n"))
serving=float(input("How many servings does this make?\n"))

print()

print("Lemonade ingredients - yields", '{:.2f}'.format(serving), "servings")
print('{:.2f}'.format(lemon), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave), "cup(s) agave nectar")

print()

print("How many servings would you like to make?")
user_amt = int(input())

make = user_amt / serving

print()

print("Lemonade ingredients - yields " '{:.2f}'.format(user_amt), "servings")
print('{:.2f}'.format(lemon * make), "cup(s) lemon juice")
print('{:.2f}'.format(water * make), "cup(s) water")
print('{:.2f}'.format(agave * make), "cup(s) agave nectar")

print()

print("Lemonade ingredients - yields " '{:.2f}'.format(user_amt), "servings")
print('{:.2f}'.format((lemon * make) / 16), "gallon(s) lemon juice")
print('{:.2f}'.format((water * make) / 16), "gallon(s) water")
print('{:.2f}'.format((agave * make) / 16), "gallon(s) agave nectar")

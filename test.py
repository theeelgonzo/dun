import sys

print("Welcome to the Dungeon.")
start = input("Are you ready to enter? Type 'Yes' or 'No' \n")

if start.lower() == "yes":
    print("Let us begin")
else:
    print("Don't mess around, nerd.")
    sys.exit()

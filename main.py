from mixing import Mixing
from heatTransfer import HeatTransfer, GetInput

def main():
    print("What scenario do you want to simulate?")
    print("""1. Mixing of two compounds and find final temperature
2. Add/remove heat to a compound to find final temperature
3. Find how much heat is required for a temperature change""")
    selection = input("""Select an option (1, 2, 3): """)

    if selection == "1":
        Mixing().mix()
    elif selection in ["2", "3"]:
        GetInput().run(selection)


main()
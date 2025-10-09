import random

print("Hello, lets play!")

options = {
    1: 'Paper',
    2: 'Rock',
    3: 'Scissors'
}

print("""Select and option:
                   
                   1) Paper
                   2) Rock
                   3) Scissors

                   """)

pred_lose = "You lose... Try again"
pred_Win = "You lose... Try again"

try:
    choose= int(input("Choose now: "))
    if choose in options:
        userchoice = options[choose]
        botoption = random.choice(list(options.values()))
        print(f'Your option was {choose} which corresponds to: {userchoice}.', 'The bot has choosen %s' % (botoption))
        print("Analyzing results...")

        if choose == botoption:
            print("Tie! Try again. None of you lose")
        elif choose == 1 and botoption == 2 or choose == 2 and botoption == 3:
            print(pred_Win)
        else:
            print(pred_lose)
        
    
except:
    print("Wrong answer please enter a number between 1-3 \n Terminating program")

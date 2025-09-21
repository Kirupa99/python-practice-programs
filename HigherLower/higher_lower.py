import random
from compare_data import sample_influencers
appreciate_words=["Wow","Great","Fantastic","Excellent","Marvelous","Brilliant"]
status=True

def check_choice(player_answer):
    if player_answer == "A" or player_answer == "a":
        player_answer = option_a
        return option_a
    elif player_answer == "B" or player_answer == "b":
        player_answer = option_b
        return option_b
    else:
        return("Enter a proper choice,'A' or 'B'.")

choice=input("Welcome to the Higher Lower Game, type 'yes' to start playing!: ")
while status:
    score = 0
    choice="yes"
    while choice=="yes":
        for item in range (len(sample_influencers)-1):
            option_a=sample_influencers[item]["name"]
            option_b=sample_influencers[item+1]["name"]
            followers_1 = sample_influencers[item]["followers"]
            followers_2 = sample_influencers[item+1]["followers"]
            player_answer=input(f"Question:Who has the maximum followers on instagram: Option A:{option_a} vs Option B:{option_b}")
            player_answer=check_choice(player_answer)
            if followers_1 > followers_2:
                correct_answer = option_a
                pos = sample_influencers[item]
                sample_influencers[item] = sample_influencers[item+1]
                sample_influencers[item+1]= pos
            else:
                correct_answer = option_b
            if  player_answer != correct_answer:
                print(f"Oops Sorry Game Over,Correct answer is:{correct_answer},Total score: {score}")
                choice = "no"
                break
            else:
                score+=1
                appreciate=random.choice(appreciate_words)
                print(f"{appreciate} Correct answer!!! Score:{score}")

    game_loop=input("Do you want to continue the game? Press 'enter' to continue or Press any other key to leave")
    if game_loop != "":
        status = False
        print("Thankyou for playing!!!")
    else:
        print("\n"*10)









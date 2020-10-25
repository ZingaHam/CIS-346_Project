#Scala Group
#the "A Game of 21"
import random

def main():
    player_score = 0
    pc_score = 0
    playing="y"
    #while loop until player says no
    while playing=="y":
        #ask player if they would like to roll, continue or quit
        print("Your score is: %d".format(player_score))
        player_ans=input("Would you like to roll, continue, or quit?(r,c,q) ")
        #simulate rolling 2(or one if player says no) six-sided dice
        #if player chooses to roll
        if player_ans.lower()=="r":
        #then simulate player and computer roll
            player_score=random.randint(1,6)+random.randint(1,6)
            pc_score=random.randint(1,6)+random.randint(1,6)
        #if player chooses to continue
        elif player_ans.lower()=="c":
        #then simulate the computer roll
            pc_score=random.randint(1,6)+random.randint(1,6)
        #if quit
        elif player_ans.lower()=="q":
        #then break the loop
            playing=''
        
    #if player has more than pc but below 21 they win
    if player_score > pc_score and player_score < 21:
        print("You win!")
        print("Final Scores:\nPlayer:%d\nComputer:%d".format(player_score,pc_score))
    #else they lose
    elif player_score == pc_score and player_score < 21:
        print("There's a tie!")
        print("Final Scores:\nPlayer:%d\nComputer:%d".format(player_score,pc_score))
    elif player_score == pc_score and player_score >= 21:
        print("There's a tie! You're at or both above 21 though.")
        print("Final Scores:\nPlayer:%d\nComputer:%d".format(player_score,pc_score))
    else:
        print("The computer wins.")
        print("Final Scores:\nPlayer:%d\nComputer:%d".format(player_score,pc_score))


main()

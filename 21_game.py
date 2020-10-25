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
        if player_score!=0:
            print("Your score is: ",player_score)
            #print("PC score",pc_score)#test
        player_ans=input("Would you like to roll, continue, or quit?(r,c,q) ")
        
        #if player chooses to roll
        if player_ans.lower()=="r":
        #then simulate player and computer roll
            player_score+=random.randint(1,6)+random.randint(1,6)
            pc_score+=random.randint(1,6)+random.randint(1,6)

        #if player chooses to continue
        elif player_ans.lower()=="c":
        #then simulate the computer roll
            pc_score+=random.randint(1,6)+random.randint(1,6)
        #if quit
        elif player_ans.lower()=="q":
        #then break the loop
            playing=''

    #if player has more than pc or pc has more than 21
    #but equal to/below 21 they win        
    if (player_score > pc_score or pc_score > 21) and player_score <= 21:
        print("You win!")
        print("Final Scores:\nPlayer:{}\nComputer:{}".format(player_score,pc_score))
    #if the scores are equal and less than 21
    elif player_score == pc_score and player_score < 21:
        print("There's a tie!")
        print("Final Scores:\nPlayer:{}\nComputer:{}".format(player_score,pc_score))
    #if the scores are equal and equal to or more than 21
    elif player_score == pc_score and player_score >= 21:
        print("There's a tie! You're at or both above 21 though.")
        print("Final Scores:\nPlayer:{}\nComputer:{}".format(player_score,pc_score))
    #if the pc score is more than the player score and less than 
    elif (pc_score > player_score or player_score > 21) and pc_score <= 21:
        print("The computer wins.")
        print("Final Scores:\nPlayer:{}\nComputer:{}".format(player_score,pc_score))
    #both over 21
    elif player_score > 21 and pc_score > 21:
        print("You're both over 21. No one won.")
        print("Final Scores:\nPlayer:{}\nComputer:{}".format(player_score,pc_score))
        


main()

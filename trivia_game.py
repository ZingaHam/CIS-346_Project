#Scala Group
#the trivia game

#question class
class Question():
    def __init__(self, question,answers,answer_number):
        self.question = question
        self.answers = answers
        self.answer_number = answer_number

    #getters
    def get_question(self):
        return(self.question)
    def get_answers(self):
        return(self.answers)
    def get_answer_number(self):
        return(self.answer_number)

    #setters
    def set_question(self, question):
        self.question=question
    def set_answers(self, answers):
        self.answers=answers
    def set_answer_number(self, answer_number):
        self.answer_number=answer_number

    def print_question(self):
        print("\n",self.question)
        i=1
        for a in self.answers:
            print("{}. {}".format(i, a))
            i=i+1

    def select_an_answer(self, number):        
        if number == self.answer_number:
            print("Congrats Right Answer")
            return True
        else:
            print("Incorrect answer")
            return False
            

def main():
    #the game
    #create an array of questions
    q0=Question("How many states are in America?", ["41","20","50","2"],3)
    q1=Question("How many toes do cats have on their front paws?",["5","1","40","2"],1)
    q2=Question("How many toes do dogs have?",["0","4","1","50"],2)
    q3=Question("Most popular Mariah Carey song:",["Shake it off","Irreplaceable","All I Want for Christmas","We Belong Together"],4)
    q4=Question("What was the orginal character limit for Twitter?",["140","20","50","2"],3)
    q5=Question("When was Spelman founded?", ["2010","1881","1750","1776"],2)
    q6=Question("What is the only U.S. state to grow coffee beans?",["Florida","California","Georgia","Hawaii"],4)
    q7=Question("What was Google’s original name? ",["Googol","Oneshot","Backrub","Typist"],3)
    q8=Question("What year was Pinterest founded in?",["2008","2009","2010","2011"],1)
    q9=Question("Hg is the chemical symbol of which element?",["Gold","Silver","Hydrogen","Mercury"],4)
    question_list=[q1,q2,q3,q4,q5,q6,q7,q8,q9]
    #scorekeeping var
    player_1=0
    player_2=0
    #loop for game
    for i in range(10):
        
        q=question_list[i]
        q.print_question()
        
        #ask for input depending on question number        
        if i%2==1:
            print("Player 2's turn")
            
            #ask for input as int
            p_input = int(input("Please input an answer number(1-4)"))
            if q.select_an_answer(p_input):
                player_2+=1    
                
            
        else:
            print("Player 1's turn")

            #ask for input as int
            p_input = int(input("Please input an answer number(1-4)"))
            if q.select_an_answer(p_input):
                player_1+=1
                
        #print scores at the end of the loop
        print("Current Scores:\n\tPlayer 1:{}\n\tPlayer 2:{}".format(player_1,player_2))

    #print scores and winner
    print("\nThe game is over!")
    if player_1>player_2:
        print("Player 1 won!")
    elif player_2>player_1:
        print("Player 2 won!")
    else:
        print("There was a tie!")
        
main()

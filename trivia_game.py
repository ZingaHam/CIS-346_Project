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
    def get_answers():
        return(self.answers)
    def get_answer_number():
        return(answer_number)

    #setters
    def set_question(self, q):
        self.question=question
    def set_answers(a):
        self.answers=answers
    def set_answer_number(a_n):
        self.answer_number=answer_number

    def print_question(self):
        print(self.question)
        i=0
        for q in question_array:
            print("%d. "+q.format(i))
            i=i+1

    def select_an_answer(self, number):        
        if number == self.answer_number:
            print("Congrats Right Answer")
        else:
            print("Incorrect answer")
            

def main():
    #the game
    #create an array of questions
    q1=Question("How many states are in America?", ["41","20","50","2"],3)
    q2=Question("How many toes do cats have on their front paws?",["5","1","40","2"],1)
    q3=Question("How many toes do dogs?",["0","4","1","50"],2)
    q4=Question("Most popular pet in South Africa:",["41","20","50","2"],3)
    q5=Question("What was the orginal char limit for Twitter?",["140","20","50","2"],3)
    question_list=[q1,q2,q3,q4,q5]
    #scorekeeping var
    player_1=0
    player_2=0
    #loop for game
    for i in range(4):
        
        q=question_list[i]
        q.print_question()
        
        #ask for input depending on question number        
        if i%2==1:
            print("Player 2's turn")
            
            #ask for input as int
            p_input = int(input("Please input an answer number(1-4)"))
            if q.get_answer_number()== p_input:
                print("Your answer was correct!")
                player_2+=1
            else:
                print("That was incorrect")    
                
            
        else:
            print("Player 1's turn")

            #ask for input as int
            p_input = int(input("Please input an answer number(1-4)"))
            if q.get_answer_number()== p_input:
                print("Your answer was correct!")
                player_1+=1
            else:
                print("That was incorrect")  
            
        
main()

#Scala Group
#the trivia game

#question class
class Question():
    def __init__(question,answers,answer_number):
        self.question = question
        self.answers = answers
        self.answer_number = answer_number

    #getters
    def get_question():
        return(self.question)
    def get_answers():
        return(self.answers)
    def get_answer_number():
        return(answer_number)

    #setters
    def set_question(q):
        self.question=question
    def set_answers(a):
        self.answers=answers
    def set_answer_number(a_n):
        self.answer_number=answer_number

    def print_question():
        print(self.question)
        i=0
        for q in question_array:
            print("%d. "+q.format(i))
            i++

    def select_an_answer(number):        
        if number == self.answer_number:
            print("Congrats Right Answer")
            r
        else:
            print("Incorrect answer")
            

def main():
    #the game
    #create an array of questions
    question_list=[]
    #scorekeeping var
    player_1=0
    player_2=0
    #loop for game
    for i in range(10):
        
        q=question[i]
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
            
        

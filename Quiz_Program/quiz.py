from colorama import init, Fore, Back, Style
from quiz_questions import *
class Quiz:
     def __init__(self):
         self.point=0
         self.flag=0
         self.question_count=1
     def intro(self):
        print("Welcome to the Quiz Master")
        print("Lets start with a brief introduction of the quiz\nThis game has 3 levels, 'Easy','Medium' and 'Hard'\n The total score is 12 points(Each level carrying 4 points,You win if you get all your answers right)")
        input("Press 'Enter' to dive into the game, All the very best!!!!")
     def start_quiz(self,level):
        if level==1:
            self.level_1()
        elif level==2:
            self.level_2()
        elif level==3:
            self.level_3()
        else:
            print(Fore.RED + "Sorry, Something went wrong, Try after sometime" + Style.RESET_ALL)
     def check_answer(self,Dict_Question,):
         global level_score
         initial_score = self.point
         for question, answer in Dict_Question.items():
             print(Fore.GREEN + "Question", self.question_count, ":" + Style.RESET_ALL)
             user_answer = input(question).strip().lower()
             self.question_count += 1
             if user_answer == answer:
                 self.point += 1
                 print("Correct answer!!!")
             else:
                 print(Fore.RED + "Oops sorry wrong answer, the right answer is:" + Style.RESET_ALL, answer)
         level_score = self.point - initial_score
         print("Total score for the level:", level_score)
     def level_1(self):
         self.check_answer(Easy_Questions)
         if self.point > 2:
             print(Fore.GREEN + "You are eligible for next Level!!!" + Style.RESET_ALL)
             self.flag = 1
         else:
             print("Sorry Game over, Better luck next time!!!")
     def level_2(self):
         self.check_answer(Medium_Questions)
         if self.point > 4:
             print(Fore.GREEN + "You are eligible for next Level!!!" + Style.RESET_ALL)
             self.flag = 2
         else:
             print(Fore.RED + "Sorry Game over, Better luck next time!!!" + Style.RESET_ALL)
     def level_3(self):
         self.check_answer(Hard_Questions)
         if self.point == 12 :
             print(Fore.GREEN + "Congratulations you have got all the answers right, You are a true Genius!!!" + Style.RESET_ALL)
         else:
             print("Your total score:",self.point,"Great Try")

obj1=Quiz()
obj1.intro()
obj1.start_quiz(1)
print(obj1.flag)
if obj1.flag==1:
    obj1.start_quiz(2)
    if obj1.flag==2:
        obj1.start_quiz(3)

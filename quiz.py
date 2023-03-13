import random
question_answers={'Entomology is the science that studies?':'insects',
                  'India lies in which continent?':'Asia',
                  'Who is known as the missile woman of India?':'Tessy Thomas',
                  'What does the ozone layer protect us from?':'UV rays',
                  'Which animal has hump on its back?':'Camel',
                  'Epsom (England) is the place associated with?':'Horse racing',
                  'Brain of computer is?':'CPU',
                  'Smallest state of India is?':'Goa',
                  '# Which is the longest river on the earth?':'Nile',
                  'Who is the Father of our Nation?':'Mahatma Gandhi',
                  'A figure with 8 sides is called?':'Octagon',
                  'National animal of India?':'Tiger',
                  ' Sun is a?':'Star','LBW is related to which sports?':'Cricket',
                  'Who is the founder of Microsoft?':'Bill Gates',
                  'Kuchipudi is the dance form of which state?':'Andhra Pradesh',
                  ' Which is largest island in the world?':'Greenland',
                  'Tsunami is a word in which language?':'Japanese',
                  'Which is largest desert in the world?':'sahara',
                  'LED stands for what?':'light emitting diode',
                  'How many players are there in an ice hockey team?':'6',
                  'which music band does jungkook belong to?':'BTS'
                 }
print("WELCOME TO THE QUIZ ;)")
while(1):
    play_status=input("Do you want to play (yes/no) : ")
    if(play_status.lower()=='no'):
        print("END OF GAME..HAVE A NICE DAY..!!")
        quit("Adios")
    elif(play_status.lower()!='yes'):
        print("INVALID INPUT..!! please enter yes/no")
        continue
    else:
        score=0
        d=question_answers.copy()
        player_name=input("Enter your name: ")
        print("OKAY {0}!! LETS BEGIN THE QUIZ.".format(player_name))
        print('''
              There would be 10 questions on general knowledge
              and your score would be evaluated at the end of 
              the quiz
              ''')
        i=1
        while(i<=10):
            print("QUESTION-{}".format(i))
            q,a=random.choice(list(d.items()))
            print(q)
            print("Answer:",end='')
            user_answer=input()
            if user_answer.lower()==a.lower():
                print("CORRECT ANSWER")
                score+=1
            else:
                print("INCORRECT ANSWER..!! THE CORRECT ANSWER IS {}".format(a.upper()))
            del d[q]
            i+=1
        print("YOU HAVE SUCCESSFULLY ")
        print("YOUR SCORE IS {} OUT OF 10".format(score))
        print('*'*10)

# Entomology is the science that studies? insects
# India lies in which continent?Answer: Asia
#  Who is known as the missile woman of India?Tessy Thomas
#  What does the ozone layer protect us from?UV rays
#  Which animal has hump on its back? Camel
# Epsom (England) is the place associated with?Horse racing  
# Brain of computer is?Answer: CPU
#  Smallest state of India is? Goa
# Which is the longest river on the earth?Answer: Nile
# Who is the Father of our Nation?Answer: Mahatma Gandhi
# A figure with 8 sides is called?':'Octagon
# National animal of India?':'Tiger
# Sun is a?':'Star
# LBW is related to which sports?':'Cricket
#  Who is the founder of Microsoft?':'Bill Gates is the founder of Microsoft.
#  Kuchipudi is the dance form of which state?':'Andhra Pradesh
#   Which is largest island in the world?':'Greenland
#   Tsunami is a word in which language?':'Japanese
#   Which is largest desert in the world?':'sahara
#   LED stands for what?':'light emitting diode
#   How many players are there in an ice hockey team?':'6
#   which music band does jungkook belong to?':'BTS
  
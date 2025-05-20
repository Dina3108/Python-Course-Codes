questions=(('How many Elements are in the periodic table?: '),('Which animal lays the largest eggs?:'),('What is the most abundant gas in the Atmosphere?:'),('How many bones are in the human body?:'))
options=(('A.116' ,'B.117', 'C.118' ,'D.119'),('A.Whale' ,'B.Crocodile','C.Elephant','D.Ostrich'),('A.Nitrogen','B.Oxygen','C.Carbon-Dioxide','D.Hydrogen'),('A.206','B.207','C.208','D.209'))
guess=[]
answers=['C','D','A',"A"]
q_no=0
score=0
for x in questions:
    print(x)
    print(options[q_no])
    g=input('Enter your Answer as Option:')
    guess.append(g.upper())
    if guess[q_no] == answers[q_no]:
     print('CORRECT')
     score+=1
    else:
       print('INCORRECT')
       print(f'Correct Answer : {answers[q_no]}')
    q_no+=1


print('----Correct Answers----')
print(answers)
print('-----Your Answers-----')
print(guess)
print(f'You Answered {((score/len(questions))*100)}% as Correct...!')
print('Congratulations....!!!')

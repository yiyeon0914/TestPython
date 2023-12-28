print('Hello yong jin, are you ready?')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3

def update_score(is_correct) :
    global score
    
    if is_correct == True :
        score +=1
        print('correct')    
    else : 
        print('Wrong answer')

if answer.lower()=='yes':
    answer=input('Question 1: Where do you work?')
    update_score(answer.lower()=='samsung')

    answer=input('Question 2: Where do you come from? ')
    update_score(answer.lower()=='korea')

    answer=input('Question 3: Where do you live?')
    update_score(answer.lower()=='san jose')

print('Thank you for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
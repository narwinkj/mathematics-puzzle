# Mathematics Puzzle Game
import random, operator
while True:
    num_1=random.randint(1,100)
    num_2=random.randint(1,100)
    operators_d={'+':operator.add(num_1,num_2),'-':operator.sub(num_1,num_2),'*':operator.mul(num_1,num_2),'**':operator.pow(num_1,num_2),'%':operator.mod(num_1,num_2),'/':operator.truediv(num_1,num_2),'//':operator.floordiv(num_1,num_2)}
    operators_l=list(operators_d.keys())
    choice=random.choice(operators_l)
    print(num_1,choice,num_2,' = ','???')
    actual_answer=operators_d[choice]
    given_answer=eval(input('Enter the Correct Answer : '))
    if given_answer==actual_answer:
        print('CONGRATULATIONZZZ...!!!!!\nYou have found the correct number...!!!!!')
    else:
        print("OPSSS.. You're not correct it seems.. Wanna try another time..???")
    print('The correct answer is :\n',num_1,' ',choice,' ',num_2,' = ',actual_answer,sep='')
    if input("Enter 'yes' to execute again..").strip().lower()=='yes':
        pass
    else:
        break

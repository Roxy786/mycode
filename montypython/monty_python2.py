#!usr/bin/env python3

round = 0   
while(True):    
    round = round + 1    
    print ('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer = input()
    if (answer == "Brian"):
        print ("Correct")
        break
    answer = (input()
    if (answer == "Shrubbery"):
        print ("You gave the super secret answer!")
    elif (round == 3):
        print ('Sorry, the answer was Brian.')
        break
    else:
        print ('Sorry. Try again!')


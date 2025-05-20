#random library is used in many simple game as logic
import random
#in the random module we have randint function that will return an integer value in the given range
number= random.randint(1,10)
print(number)

low=1
high=100
print(random.randint(low,high))

game_choices=['rock','paper','scissors']
#we have choice function that will return any one of value in the list 
print(random.choice(game_choices))

cards=['1',2,3,'4','J','Q',"K"]
random.shuffle(cards)
#shuffle function will return a list by shuffling all the elements in the given list
print(cards)
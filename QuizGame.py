# Quiz Game
# Author: Matthew Wong
# Date: 2/13/2019

score_tally = 0

a = input("Do you want to play a game? ")
if a == ("yes").lower():
    print("correct")
    score_tally += 1
else: 
    print("correct")
    score_tally += 1
    
print("")    
    
b = input("What is 89 + 22/2? ")
if b == ("100").lower():
    print("true")
    score_tally += 1
else:
    print("false")

print("")    
    
c = input("how many letters are in the word 'one'? ")
if c == ("3").lower():
    print("true")
    score_tally += 1
else: 
    print("incorrect")
    
print("")  

d = input("what can love be classified as? ")
if d == ("emotion").lower():
    print("correcto")
    score_tally += 1
else: 
    print("wrong")

print("")

e = input("translate 'me gusta tu': ")
if e == ("i like you").lower():
    print("true")
    score_tally += 1
else: 
    print("nope")
    
print("")
    
new_score_tally = (score_tally / 5) * 100

print("Your overall score is, " + str(new_score_tally) + "%")
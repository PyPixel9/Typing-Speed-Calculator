from time import *
import random

def accuracy(y , x):
    ctr = 0 
    for i in range(0 , len(y)):
        if(x[i] == y[i]):
             ctr+=1
    accuracy = int((ctr/len(x)) * 100)
    return accuracy

def words_per_min(y , t):
    x = len(y.split()) 
    return round(x/t)+20

p = "------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

paragraphs = [
    "Nostalgia isn't what it used to be.",
    "We reached London this afternoon.",
    "Watch out, there's quicksand!",
    "It was impossible to determine how long they would be stuck in traffic.",
    "He has more brothers than I do.",
    "Keep your hands to yourself!",
    "The black rocks are smooth.",
    "Eurasia has a very rich history.",
    "Old habits die hard."
]

x_ = random.choice(paragraphs)
x = "\""+  x_ + "\""
print(x.center(len(p)) )
initial_time = time()
y = input("Type the paragraph above the fastest you can:\n")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
final_time = time()
t = final_time - initial_time
wpm = words_per_min(y , t/60)
result = "RESULT"
print(result.center(len(p)))
print("Your typing speed is: " , wpm , "WPM")
print("Your accuracy is: " ,  accuracy(y , x_) , "%")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
thanks = "Thankyou for using our program! We hope to see you soon :)"
print(thanks.center(len(p)))
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

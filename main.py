import random
import sys
import cv2
from time import sleep





# this is the vocabulary list that the words will be pulled from
vocabulary_list = ["cat"]


# this dictionary hold the file paths that lead to the ASL hand shape images
asl_letters = {
    "a":"/Users/nilefahmy/PycharmProjects/fingerspell/a.gif",
    "c":"/Users/nilefahmy/PycharmProjects/fingerspell/c.gif",
    "t":"/Users/nilefahmy/PycharmProjects/fingerspell/c.gif",
}


# this variable holds the current word that is being Displayed in the UI
current_word = random.choice(vocabulary_list)


# This action should display the current word in ASL finger spelling
def que_word():
    for letters in current_word:




que_word()


# this function will promt the user to spell the that was fingerspelled to them in english
def get_user_answer():
    user_guess = input("spell the word you saw: ")
    print("Booyah!")
    return user_guess


user_answer = get_user_answer()

print(user_answer)


# This function will check the users answer against the current word
def check_answer(user_answer, current_word):
    if user_answer == current_word:
        print("correct")
    else:
        print("incorect")


check_answer(current_word=current_word, user_answer=user_answer)

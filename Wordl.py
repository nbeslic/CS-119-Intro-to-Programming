# Project #3
# Created by: Natalija Beslic
# Submitted: April 8, 2023

# TO DO 1
import random

def get_word()->str:
    all_words = ['above','blame','corny','dress','email','flail','glass','horse','igloo','judge','kebab','lilac','moose','never','olive','prize','query','react','shrub','toxic','untie','vigor','wordl','yield','zesty']
    my_word = random.choice(all_words)
    return my_word

# TO DO 2
#def get_guess()->str:
#    guess = str(input('Your Guess: '))
#    guess = guess.lower()
#    return guess

# TO DO 3
def print_guess(value:str) -> None:
    print(value[0] + '  ' + value[1] + '  ' + value[2] + '  ' + value[3] + '  ' + value[4])

# TO DO 4
def get_diff(word:str, guess:str)-> list:
    i = 0
    diffs = []
    while i < len(word):
        if word[i] == guess[i]:
            diffs.append('g')
        elif guess[i] in word:
            diffs.append('y')
        else:
            diffs.append('r')
        i += 1
    return diffs

# TO DO 5
def print_diff(diffs:list) -> None:
    i = 0
    emojis = ''
    while i < len(diffs):
        if diffs[i] == 'g':
            emojis += '🟢 '
        elif diffs[i] == 'y':
            emojis += '🟡 '
        else:
            emojis += '🔴 '
        i += 1
    print(emojis)   

# TO DO 6
def play_turn(word:str) -> bool:
    won = False
    guess = get_guess()
    print_guess(guess)
    print_diff(get_diff(word, guess))
    if word == guess:
        won = True
    return won

# TO DO 7
#def play_game() -> None:
#    correct_word = get_word()
#    has_won = False
#    turn = 0
#    while has_won != True:
#        turn += 1
#        if turn == 7:
#            print(f"Out of turns, the word was: {correct_word}")
#            return
#        print(f"\nTURN {turn}:")
#        has_won = play_turn(correct_word)
#    if has_won == True:
#        print(f"you've won! it took {turn} turns")
#        return


# Extra Credit 1
def get_guess()->str:
    guess = str(input('Your Guess: '))
    while len(guess) != 5 or guess.isalpha() == False:
        print(f"{guess} is an invalid guess")
        guess = str(input('Your Guess: '))
    guess = guess.lower()
    return guess


# Extra Credit 2
def play_game(turns=6) -> None:
    correct_word = get_word()
    has_won = False
    turn = 0
    while has_won != True:
        turn += 1
        if turn == turns + 1:
            print(f"Out of turns, the word was: {correct_word}")
            return
        print(f"\nTURN {turn}:")
        has_won = play_turn(correct_word)
    if has_won == True:
        print(f"you've won! it took {turn} turns")
        return




## testing
#guess = get_guess()
#print_guess(guess)
#word = get_word()
#print(word , get_diff(word, guess))
#print_diff(get_diff(word, guess))

#random.seed(1)
#play_game(3)



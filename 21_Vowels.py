# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ")
user_word = user_word.upper()
vow = ['A','E','I','O','U']

for letter in user_word:
    # Complete the body of the for loop.
    if letter not in vow:
        print(letter)
    else:
        continue
        
        

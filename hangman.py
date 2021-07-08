import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings 
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

def remove_dups(secret_word) :
  l = ''
  for char in secret_word :
    if char not in l :
      l += char 
  return l

def is_word_guessed(secret_word, letters_guessed):
  for char in secret_word :
    if char not in letters_guessed :
      return False
  return True
 
def get_guessed_word(secret_word, letters_guessed):
  l = ""
  for char in secret_word :
    if char in letters_guessed :
      l += char
    else :
      l += '_ '
  return l

def get_available_letters(letters_guessed):
  s = string.ascii_lowercase
  for char in letters_guessed :
    s = s.replace(char,'')
  return s  

def hangman(secret_word):
  print('Welcome to the game Hangman !')
  print('I am thinking of a word that is',len(secret_word),'letters long')
  print('you have 3 warnings left')
  print('----------')
  no_of_warnings = 3
  no_of_guesses = 6
  letters_guessed = []
  while no_of_guesses > 0 :
    print('you have',no_of_guesses,'guesses left')
    print('Available letters',get_available_letters(letters_guessed))
    s = input('please guess a letter: ')
    if s not in letters_guessed : 
      if s in string.ascii_letters :
        s = s.lower()
        if s in 'aeiou' and s not in secret_word:
            no_of_guesses -= 2
        if s not in 'aeiou' and s not in secret_word:
            no_of_guesses -= 1 
        letters_guessed += list(s)
        if s in secret_word :
          print('good guess: ',end = '')
        else :
          print('Oops! That letter is not in my word:',end = '')
    else :
      no_of_warnings -= 1
      if no_of_warnings >= 0 :
        print('Oops! you have already guessed that letter. You have',no_of_warnings,'warnings left')
      else :
        print('Oops! you have already guessed that letter. You have no warnings left')
        print('so you lose one guess: ',end = '')
        no_of_guesses -= 1
    if s not in string.ascii_letters :
      no_of_warnings -= 1
      if no_of_warnings >= 0 :
        print('Oops! that is not a valid letter. You have',no_of_warnings,'warnings left',end = '')
      else :
        print('Oops! that is not a valid letter. You have no warnings left')
        print('so you loose one guess: ',end = '')
        no_of_guesses -= 1
    print(get_guessed_word(secret_word,letters_guessed))
    if is_word_guessed(secret_word,letters_guessed) :
      print('Congratulations, you won!')
      score = no_of_guesses * len(remove_dups(secret_word))
      print('your total score for this game is:',score)
      break
    print('----------')
  if not is_word_guessed(secret_word,letters_guessed) :
    print('Sorry you ran out of guesses. The word was',secret_word)    

def match_with_gaps(my_word, other_word):
  s = my_word.replace(' ','')
  if len(s) != len(other_word):
    return False
  for i in range(len(s)) :
    if s[i] != '_' :
      if s[i] != other_word[i] :
        return False
  return True

def show_possible_matches(my_word):
  s = ''
  for words in wordlist :
    if match_with_gaps(my_word,words) :
      print(words,end = ' ')
      s += words
  if len(s) == 0 :
    print('no matches found')
  print()

def hangman_with_hints(secret_word):
  print('Welcome to the game Hangman !')
  print('I am thinking of a word that is',len(secret_word),'letters long')
  print('you have 3 warnings left')
  print('----------')
  no_of_warnings = 3
  no_of_guesses = 6
  letters_guessed = []
  while no_of_guesses > 0 :
    print('you have',no_of_guesses,'guesses left')
    print('Available letters',get_available_letters(letters_guessed))
    s = input('please guess a letter: ')
    if s == '*' :
      show_possible_matches(get_guessed_word(secret_word,letters_guessed))
    else :
      if s not in letters_guessed : 
        if s in string.ascii_letters :
          s = s.lower()
          if s in 'aeiou' and s not in secret_word:
              no_of_guesses -= 2
          if s not in 'aeiou' and s not in secret_word:
              no_of_guesses -= 1 
          letters_guessed += list(s)
          if s in secret_word :
            print('good guess: ',end = '')
          else :
            print('Oops! That letter is not in my word:',end = '')
      else :
        no_of_warnings -= 1
        if no_of_warnings >= 0 :
          print('Oops! you have already guessed that letter. You have',no_of_warnings,'warnings left')
        else :
          print('Oops! you have already guessed that letter. You have no warnings left')
          print('so you lose one guess: ',end = '')
          no_of_guesses -= 1
      if s not in string.ascii_letters :
        no_of_warnings -= 1
        if no_of_warnings >= 0 :
          print('Oops! that is not a valid letter. You have',no_of_warnings,'warnings left',end = '')
        else :
          print('Oops! that is not a valid letter. You have no warnings left')
          print('so you loose one guess: ',end = '')
          no_of_guesses -= 1
      print(get_guessed_word(secret_word,letters_guessed))
      if is_word_guessed(secret_word,letters_guessed) :
        print('Congratulations, you won!')
        score = no_of_guesses * len(remove_dups(secret_word))
        print('your total score for this game is:',score)
        break
      print('----------')
  if not is_word_guessed(secret_word,letters_guessed) :
    print('Sorry you ran out of guesses. The word was',secret_word)    

if __name__ == "__main__":
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)   
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

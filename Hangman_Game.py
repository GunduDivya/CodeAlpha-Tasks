import random
import threading
def choose_word():
    words=['python','developer','fresher','experience','coding']
    return random.choice(words)
#function to display the current state of the hangman
def display_hangman(tries):
    stages=[
        """
            ------
            |    |
            |    O 
            |   /|\\
            |   / \\
            |
        
        """,
        """
                    ------
                    |    |
                    |    O 
                    |   /|\\
                    |   / 
                    |
    
        """,
        """
                    ------
                    |    |
                    |    O 
                    |   /|
                    |   
                    |
    
        """,

        """
                    ------
                    |    |
                    |    O 
                    |    |
                    |   
                    |
    
        """,
        """
                    ------
                    |    |
                    |    O 
                    |   
                    |   
                    |
    
        """,
        """
                    ------
                    |    |
                    |    
                    |   
                    |   
                    |
    
        """,
        """
                    ------
                    |    
                    |    
                    |   
                    |   
                    |
    
        """
    ]
    return stages[tries]
def time_limit_exceede():
    print('\n Time is up! you did not guess in time')
    raise SystemExit
def play():
    word=choose_word()
    word_completion='_'* len(word)
    guessed=False
    guessed_letters=[]
    tries=6
    print('welcome to Hangman!')
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries>0:
        timer=threading.Timer(10.0,time_limit_exceede)
        timer.start()
        guess=input("please enter a letter(you have 10 seconds):").lower()

        timer.cancel()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print('you ve already guessed that letter')
            elif guess not in word:
                print('Incorrect guess.')
                tries-=1
                guessed_letters.append(guess)
            else:
                print('good guess!')
                guessed_letters.append(guess)
                word_completion="".join([letter if letter in guessed_letters else '_' for letter in word])
                if "_" not in word_completion:
                    guessed=True
        else:
            print("Invalid input.Please enter a single letter.")
        print(display_hangman(tries))
        print(word_completion)
        print('\n')
    if guessed:
        print('congratulations! you have guessed the word :'+word)
    else:
        print('Sorry, youve lost. the word was:'+word)
if __name__=='__main__':
    play()
    
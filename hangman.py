import os
import random
import unicodedata

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def presentation():
    # Function to print ASCII art from presentation.txt file
    with open('./hangman_utils/presentation.txt', "r", encoding="UTF-8") as p:
        print(p.read())

def print_separator():
    print('-'*20,'\n')

def show_head_message(message):
    print(f'{"="*15} {message} {"="*15}')    

def init_game():
    # Function to get word from data.txt file and normalize the string
    words = []
    lines = ""
    # Read the file
    with open('./hangman_utils/data.txt', "r", encoding="utf-8") as p:
        for word in p:
            words.append(word.replace('\n',''))

    # Get a random word        
    game_word = (random.choice(words))
    print_separator()

    # Count word length and show to user
    for i in game_word:
        lines += "_ "  
    print("TU PALABRA CONTIENE "+ str(len(game_word))+ " LETRAS: "+lines)

    # Return normalized word, without special characters
    return (unicodedata.normalize('NFKD', game_word).encode('ASCII', 'ignore').decode())


def show_hangman(oportunities):
    # Print the hangman animation, based on the oportunities

    # Get the animation from file and get lines based on the oportunity number
    with open('./hangman_utils/animation.txt', "r", encoding="UTF-8") as a:
                for index, line in enumerate(a):
                    if index  >= oportunities * 8 and index <= oportunities * 8 + 7:
                        print(line.replace("\n",""))


def input_has_error(input):

    # Verify if the input is valid or not. Only one character and need to be 
    if input.isnumeric() or len(input) != 1 or input not in LETTERS:
        return True


def show_word(out_word):
    
    # Function to show word based on user input
    out_line = ""
    for ok_letter in out_word:

        # If input is correct, show the letter, else show an undescore
            if ok_letter:
                out_line += ok_letter + " " 
            else:
                out_line += "_ "
    return (out_line+"\n")        


def play(word):
    # Game process 
    out_word = []
    end = False
    oportunities = 0
    show_hangman(0)
    letter_list = list(word)
    out_word = []

    # Create a list with word size and with a False value in every cell
    for i in letter_list:
        out_word.append(False)

    # Start user interaction    
    while True:
        in_letter = str.lower(input('Ingresa una letra: '))

        #Validate user input
        if  input_has_error(in_letter):
            print("Entrada invalida. Introduzca solamente UNA letra de la A a la Z")
            continue
        os.system('clear')
        correct = False
        
        for index, word_letter in enumerate(letter_list):
            
            # Validate if user's input exist into the word
            if word_letter == in_letter:
                out_word[index] = word_letter
                correct = True                
        if not correct:
            show_head_message("ERROR")
            oportunities = oportunities + 1

            # Validate if user have oportunities left  
            if oportunities == 6:
               show_head_message("GAME OVER")
               print('La palabra correcta es: '+show_word(word))
               show_hangman(oportunities)
               break
        else:
            show_head_message("CORRECTO")
        show_head_message(f'INTENTO  {str(oportunities+1)} de 7')
        show_hangman(oportunities)

        # If there is no False value in the list, show winner message        
        if False not in out_word:
            os.system('clear')
            show_head_message("YOU WIN")
            print('La palabra es: '+show_word(word))
            break
        print(show_word(out_word))


def run():
    presentation()
    word_game = init_game()
    play(word_game)


if __name__=='__main__':
    run()
import os
import random
import unicodedata

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def presentation():
    with open('./hangman_utils/presentation.txt', "r", encoding="UTF-8") as p:
        print(p.read())


def init_game():
    words = []
    lines = ""
    with open('./hangman_utils/data.txt', "r", encoding="utf-8") as p:
        for word in p:
            words.append(word.replace('\n',''))
            
    game_word = (random.choice(words))
    print("------------------------------------------------\n")
    for i in game_word:
        lines += "_ "  
    print("TU PALABRA CONTIENE "+ str(len(game_word))+ " LETRAS: "+lines)
    return (unicodedata.normalize('NFKD', game_word).encode('ASCII', 'ignore').decode())


def show_hangman(oportunities):
    with open('./hangman_utils/animation.txt', "r", encoding="UTF-8") as a:
                for index, line in enumerate(a):
                    if index  >= oportunities * 8 and index <= oportunities * 8 + 7:
                        print(line.replace("\n",""))


def input_has_error(input):
    if input.isnumeric() or len(input) != 1 or input not in LETTERS:
        return True


def show_word(out_word):
    out_line = ""
    for ok_letter in out_word:
            if ok_letter:
                out_line += ok_letter + " " 
            else:
                out_line += "_ "
    return (out_line+"\n")        


def play(word):
    out_word = []
    end = False
    oportunities = 0
    show_hangman(0)
    letter_list = list(word)
    out_word = []
    for i in letter_list:
        out_word.append(False)
    while True:
        in_letter = str.lower(input('Ingresa una letra: '))
        if  input_has_error(in_letter):
            print("Entrada invalida. Introduzca solamente UNA letra de la A a la Z")
            continue
        os.system('clear')
        correct = False
        
        for index, word_letter in enumerate(letter_list):
            if word_letter == in_letter:
                out_word[index] = word_letter
                correct = True                
        if not correct:
            print("============== ERROR ==============\n")
            oportunities = oportunities + 1  
            if oportunities == 6:
               print('============ GAME OVER ============\n')
               print('La palabra correcta es: '+show_word(word))
               show_hangman(oportunities)
               break
        else:
            print("============== CORRECTO ==============\n")
        print("======= INTENTO " + str(oportunities+1) + ' de 7 =======')   
        show_hangman(oportunities)        
        if False not in out_word:
            os.system('clear')
            print('============ YOU WIN! ============\n')  
            print('La palabra es: '+show_word(word))
            break
        print(show_word(out_word))


def run():
    presentation()
    word_game = init_game()
    play(word_game)


if __name__=='__main__':
    run()
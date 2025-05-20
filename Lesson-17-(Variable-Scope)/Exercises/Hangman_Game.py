import random
words=('Dinakar','Amma','Appa','Sripathi','Hariniii')
hangman_art={0: (' ',
                ' ',
                ' '),
            1: (' o',
                ' ',
                ' '),
            2: (' o',
                '|',
                ' '),
            3: (' o',
               '/| ',
               ' '),
            4: (' o',
               '/|\\',#Here double backslash only work with only single backslash consider it as Escape Sequence
               ' '),
            5: (' o',
              '/|\\',
              '/|'),
            6: (' o',
               '/|\\',
               '/|\\')}
def display_man(wrong_guesses):
    for x in hangman_art[wrong_guesses]:
        print(x)
def display_hint(hint):
    print(' '.join(hint))
def display_answer(answer):
    print(' '.join(answer))
def main():
    answer=random.choice(words)
    hint=['_']*len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running=True
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess=input('Enter a Letter : ')
    
        if len(guess)!=1 or not guess.isalpha():
          print('Invalid Input')
          continue

        if guess in guessed_letters:
           print(f'{guess} is Already Guessed')
           continue
        guessed_letters.add(guess)

        if guess in answer:
          for y in range(len(answer)):
            if answer[y]==guess:
              hint[y]=guess
        else:
           wrong_guesses+=1

        if '_' not in hint:
           display_man(wrong_guesses)
           display_answer(answer)
           print('You WIN...!')
           is_running=False   
        elif (wrong_guesses>=len(hangman_art)-1):
           display_man(wrong_guesses)
           display_answer(answer)
           print('You LOSE...!')
           is_running=False
    else:
        print('Wrong Answer')

if __name__=='__main__':
    main()
import random

def draw_hang_loser():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|        /|\   \n")
    print("|        / \   \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head_body_legs_la():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |\   \n")
    print("|        / \   \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head_body_legs():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |    \n")
    print("|        / \   \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head_body_ll():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |    \n")
    print("|          \   \n")
    print("|              \n")
    print("|              \n")   

def draw_hang_head_body():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |    \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")

def draw_hang_scaffold():
    print(" _________     \n")
    print("|         |    \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")

def draw_hangman(state):
    if state == 0:
        draw_hang_scaffold()
    elif state == 1:
        draw_hang_head()
    elif state == 2:
        draw_hang_head_body()
    elif state == 3:
        draw_hang_head_body_ll()
    elif state == 4:
        draw_hang_head_body_legs()
    elif state == 5:
       draw_hang_head_body_legs_la()
    elif state == 6:
        draw_hang_loser()
        
#returns True if the string has no underscores in it  "_" .  
#else returns false if the string has any underscores in it.  
def blanks_gone(s):
    if s.find('_') == -1:
        return True
    else:
        return False

def replace_all(orig, working, ch):
  done = False
  count = 0
  while not done:
    idx = orig.find(ch)
    if idx != -1:
      count = count + 1
      orig = orig[:idx] + "_" + orig[idx+1:]
      working = working[:idx] + ch + working[idx+1:]
    else:
      done = True
  return count != 0, orig, working 
  
def main():
    sentence = random.choice((open('Words.txt').read()).strip().lower().split())
    places = ""
    state = 0
    #for loop to add a “_” to places for every character in sentence
    for c in sentence:
        places = places + "_"
    winner = False
    while winner == False and state != 6:
        draw_hangman(state)
        print (places)
        
        char = input("Enter a character: ")


        success, sentence, places = replace_all(sentence, places, char)

        print("4")
        
        if success == False:
            state += 1
            print("5")
            
        if blanks_gone(places) == True:
            winner = True
            print("6")
        print("7")

    draw_hangman(state)
    
    if (winner == True):
        print("CONGRATS! You Win!")
    else:
        print("Sorry, you lose :-(")
        
main()
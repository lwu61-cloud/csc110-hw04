# ------------------------------------------------------
#        Name: (Lynn Wu)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Read text from the user and check whether the input string includes the secret word or 'dog'/ 'Dog';
        if not, then ask the user to try again.    
    """
    while True:
        text = input("Enter a sentence: ") #get a string from the user
        if secret_word in text:  #check if the user inputs include the secret word
            print("You used the secret word!")
            break
        elif "dog" in text or "Dog" in text: #check if the user inputs include dog or Dog
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        else: #if nothing is included, repeat
            print("Try again")
    
    
# Task 2
def check_greater():
    """ Get two integers from the user and compare which one is greater. """
    stop = False
    while not stop:
        a = int(input("Give me the first integer: ")) # get two integers from the user
        b = int(input("Give me the second integer: "))
        if a>b:   # check if the first integer is greater
            print("First is Greater")
            print("Done")
            stop=True
        elif a<b: # check if the second integer is greater
            print("Second is Greater")
            print("Done")
            stop=True
        else: # repeat the steps if the two integers are equal
            print("Try again")
        


# Task 3
def get_special_numbers():
    """ A loop to examine and print any odd integer between 1 and 40 that is multiple of 3 but is not a multiple of 5. """
    for i in range(1, 41):
        if i%2 != 0 and i%3 == 0 and i%5 != 0:
            print(i)


# Task 4.a
def my_for_loop():
    """ Ask a string from the user and check if each letter in the string is vowel"""
    user_input = input("Enter a string: ")
    vowel=["a","e","i","o","u"]
     # if length of string is not between 2 and 5,or it contains space, immediately return
    if len(user_input) not in range(2,6):
        print("bad word")
        return
    elif " " in user_input:
        print("bad word")
        return
    # if the length of string is between 2 and 5 and does not contain space
    elif len(user_input) in range(2,6):
        for letter in user_input: # check whether each letter is vowel or constant
            if letter in vowel:
                print(f"{letter} is a vowel")
            else:
                print(f"{letter} is a consonant")

# Task 4.b
def my_while_loop():
    """ Respond according to user's choices: a for repeat the menu, b for "Goodbye" and return, c for exit the program;
        other invaid input would lead to "Try again" and repeated menu.
    """
    while True: # construct a loop
        choice = input("Select from 'a', 'b', and'c': ")
        #if user choice is valid, respond according to their choice
        if choice == 'a':
            continue
        elif choice == 'b':
            print("Goodbye")
            return
        elif choice == 'c':
            exit()
        #if choice is not valid, repeat the loop
        else:
            print("try again")
            continue

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

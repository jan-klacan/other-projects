import sys

# HELPER FUNCTION TO SLICE KEYWORD CHARACTERS INTO A LIST
    # - USED IN ENCRYPTION AND DECRYPTION FUNCTIONS -
def keyword_characters_into_list(keyword):
    kw_char_list = []
    for character in keyword:
        if character.isupper():
            zero_index_base = ord("A")
        else:
            zero_index_base = ord("a")
        kw_char_normalized_position = (ord(character) - zero_index_base) % 26
        kw_char_list.append(kw_char_normalized_position)
    return kw_char_list
##

# FUNCTION FOR ENCRYPTION WITH A KEYWORD
def vigenere_encrypt(text_raw, keyword):
    keyword_characters = keyword_characters_into_list(keyword)
    
    text_encrypted = ""
    keyword_length = len(keyword)

    letter_increment_index = 0
    
    for character in text_raw:
        if character.isalpha():
            if character.isupper():
                zero_index_base = ord("A")
            else:
                zero_index_base = ord("a")
            shift_by = keyword_characters[letter_increment_index % keyword_length]
            position_shifted = (ord(character) - zero_index_base + shift_by) % 26 + zero_index_base
            text_encrypted += chr(position_shifted)
            letter_increment_index += 1
        else:
            text_encrypted += character
    return text_encrypted
##

# FUNCTION FOR DECRYPTION WITH A KEYWORD
def vigenere_decrypt(text_encrypted, keyword):
    keyword_characters = keyword_characters_into_list(keyword)

    text_decrypted = ""
    keyword_length = len(keyword)

    letter_increment_index = 0

    for character in text_encrypted:
        if character.isalpha():
            if character.isupper():
                zero_index_base = ord("A")
            else:
                zero_index_base = ord("a")
            shift_by = keyword_characters[letter_increment_index % keyword_length]
            position_shifted = (ord(character) - zero_index_base - shift_by) % 26 + zero_index_base
            text_decrypted += chr(position_shifted)
            letter_increment_index += 1
        else:
            text_decrypted += character
    return text_decrypted
##

# MAIN RUNNING INTERFACE FUNCTION
def run_main():
    print("--- Welcome to the Vigenere cipher encryption and decryption interface. ---")

    # Input handling for user's fork choice of either encryption or decryption
    while True:
        try:
            print("\n-- To encrypt with a known keyword, enter 0. -- \n-- To decrypt with a known keyword, enter 1. --")
            fork_choice = int(input("Enter value: "))
            if fork_choice in [0, 1]:
                break
            else:
                print("Invalid input. Please enter 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter 0 or 1.")

    # Determine the user action description string, for later use
    user_choice_str = None
    if fork_choice == 0:
        user_choice_str = "encrypt"
    elif fork_choice == 1:
        user_choice_str = "decrypt"

    # Input handling and storage of user messages
    while True:
        try:
            messages_number = int(input(f"Please enter the number of separate messages to {user_choice_str}: "))
            if messages_number < 0:
                print("The number of messages must be a positive integer. Please try again.")
            elif messages_number == 0:
                while True:
                    try:
                        print("-- You entered 0 messages. --")
                        print("-- Enter 0 to exit the process or 1 to try entering a valid number of messages. --")
                        exit_choice = int(input("Enter value: "))
                        if exit_choice == 0:
                            print("Exiting the process.")
                            sys.exit()
                        elif exit_choice == 1:
                            break
                        else:
                            print("Invalid input. Please enter 0 to exit the process or 1 to continue.")
                    except ValueError:
                        print("Invalid input. Please enter 0 to exit the process or 1 to continue.")
            else:
                break
        except ValueError:
            print("Invalid input. The number of messages must be a positive non-zero integer.")

    messages = {}
    for n in range(messages_number):
        text_user = input(f"Enter message {n+1}: ")
        messages[n] = text_user

    # Input handling for user's choice of keyword
    while True:
        keyword_user_candidate = input(f"Enter keyword to {user_choice_str} (must consist of valid letters): ")
        if keyword_user_candidate.isalpha():
            keyword_user_final = keyword_user_candidate
            break
        else:
            print("Invalid input. Keyword must consist of valid letters.")

    # Perform chosen action: encryption or decryption
    if fork_choice == 0:
        for index, message in messages.items():
            text_user_encrypted = vigenere_encrypt(message, keyword_user_final)
            print(f"\nEncrypted message {index+1}: ")
            print(text_user_encrypted)

    elif fork_choice == 1:
        for index, message in messages.items():
            text_user_decrypted = vigenere_decrypt(message, keyword_user_final)
            print(f"\nDecrypted message {index+1}: ")
            print(text_user_decrypted)
##

# CALL OF THE MAIN RUNNING INTERFACE FUNCTION, AFTER CHECK IF THE SCRIPT RUN DIRECTLY
if __name__ == "__main__":
    run_main()
##
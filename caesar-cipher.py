import sys

# FUNCTION FOR ENCRYPTION WITH KNOWN SHIFT-BY VALUE
def caesar_encrypt(text_raw, shift_by):
    text_encrypted = ""
    for character in text_raw:
        if character.isalpha():
            if character.isupper():
                zero_index_base = ord("A")
            else:
                zero_index_base = ord("a")
            position_shifted = (ord(character) - zero_index_base + shift_by) % 26 + zero_index_base
            text_encrypted += chr(position_shifted)
        else:
            text_encrypted += character
    return text_encrypted
##

# FUNCTION FOR DECRYPTION WITH KNOWN SHIFT-BY VALUE
def caesar_decrypt(text_encrypted, shift_by):
    return caesar_encrypt(text_encrypted, -shift_by)
##

# MAIN RUNNING INTERFACE FUNCTION 
def run_main():
    print("--- Welcome to the Caesar cipher encryption and decryption interface. ---")
    
    # Input handling for user's fork choice of either encryption or decryption
    while True:
        try:
            print("\n-- To encrypt with a known shift-by value, enter 0. -- \n-- To decrypt with a known shift-by value, enter 1. -- \n-- To execute brute force attack, enter 2. --")
            fork_choice = int(input("Enter value: "))
            if fork_choice in [0, 1, 2]:
                break
            else:
                print("Invalid input. Please enter 0, 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 0, 1 or 2.")
        
    # Determine the user action description for later use
    user_choice_str = None
    if fork_choice == 0:
        user_choice_str = "encrypt"
    elif fork_choice == 1:
        user_choice_str = "decrypt"
    elif fork_choice == 2:
        user_choice_str = "execute brute force attack on"

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

    # Input handling for user's choice of shift-by value, if applicable
    while True:
        if fork_choice in [0, 1]:
            try:
                shift_by_user = int(input("Enter the shift-by value (positive integer for right shift, negative integer for left shift): "))
                break
            except ValueError:
                print("Invalid input. Shift-by value must be an integer.")
        else:
            break

    # Perform chosen action: encryption, decryption, or brute force attack
    if fork_choice == 0:
        for index, message in messages.items():
            text_user_encrypted = caesar_encrypt(message, shift_by_user)
            print(f"\nEncrypted message {index+1}: ")
            print(text_user_encrypted)

    elif fork_choice == 1:
        for index, message in messages.items():
            text_user_decrypted = caesar_decrypt(message, shift_by_user)
            print(f"\nDecrypted message {index+1}: ")
            print(text_user_decrypted)

    elif fork_choice == 2:
        for index, message in messages.items():
            for shift_by_test in range(26):
                text_user_brute_force = caesar_decrypt(message, shift_by_test)
                print(f"\nBrute force for normalized shift-by value {shift_by_test} for message {index+1}: ")
                print(text_user_brute_force)  
##

# CALL OF THE MAIN RUNNING INTERFACE FUNCTION, AFTER CHECK IF THE SCRIPT RUN DIRECTLY
if __name__ == "__main__":
    run_main()
##
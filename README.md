These are my other coding projects. See ordered descriptions for each project below.


# 001-caesar-cipher

This is a simple Python implementation of the Caesar cipher technique. I implemented an interface for the user of the script so that when run, the user is presented with choices with the ultimate purpose of one of the three below:
1. Encrypt a message with a user-specified shift value
2. Decrypt a message with a user-specified shift value
3. Execute brute force attack on a decrypted message (no shift value specified)
(Note: in the code I call the shift value "shift-by".)

The code includes:
- a function for encryption
- a function for decryption
- a function for the main running interface with input handling so that the user's choices are constrained to predetermined ranges. 

The brute force attack is built into the main running interface function.


# 002-vigenere-cipher

This is a simple Python implementation of the Vigenère cipher technique. I implemented an interface for the user of the script so that when run, the user is presented with choices with the ultimate purpose of one of the two below:
1. Encrypt a message with a user-specified keyword
2. Decrypt a message with a user-specified keyword

The code includes:
- a helper function to slice the characters of the keyword into a list
- a function for encryption
- a function for decryption
- a function for the main running interface with input handling so that the user's choices are constrained to predetermined ranges
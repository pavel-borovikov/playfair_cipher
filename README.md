# playfair_cipher
Ciphers or deciphers a message with a keyword.
Any character used must be included in the valid characters.
The amount of characters must be a squared number. The grid size should be equal to that number's square root.

The cipher functions does NOT account for doubled letters during the ciphering process.
When using the Playfair cipher, the message's letters are grouped into 2 letter groups. 
If both of those letters are the same, there is no way to cipher them, thus a spliter character is added after the first occurrence of the letter.
This action must be done manually beforehand, in the message string.

The cipher function also does NOT verify that there is an even amount of characters in a string that is to be ciphered.
Again, because the letters are groups of 2, if the message is of an uneven length, it cannot be ciphered.
This action must be done manually in the message string.



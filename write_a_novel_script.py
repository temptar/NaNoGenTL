# This script will write a novel automatically. It probably
# won't make much sense but...
# See ReadMe for requirements
# See licence for usage. 

# import statements
import os
import time
import datetime
import random
import string

# global variables

proceed = True
cleartext = "Or it's inconsistent and thus flawed"
alphaclear=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

cipher = []
decrypt = []

crypttext = ""
deconstruct = ""

# Code

# general subroutines

def create_key():
    # This takes the mapping, performs some arithmetic against the numeric 
    # values in the key, adding either 1 or 2 to the index values of the 
    # mapping. 1 or 2 is added as a checkdigit; if 1 was added to the index
    # valuesm, then 2 is added as a checkdigit, and vice versa. 
    global decrypt
    global deconstruct
    layer_key = random.randint(1,2)
    decrypt = [x+layer_key for x in decrypt]
    if layer_key == 1:
        decrypt.append(2)
    else:
        decrypt.append(1)
    deconstruct = '$'.join(map(str, decrypt))

def create_encryption_key():
    # this creates the encryption mapping to generate a mapping from
    # a cleartext alphabet to a scrambled alphabet. 
    # scrambled alphabet will consist of fewer letters than the
    # cleartext alphabet and the number of scrambled letters is
    # randomly selected between 1 and 25. 
    # the available letter for scrambling are drawn from the start
    # of the alphabet to the index of whatever the random number is, 
    # so if 15 were drawn, every letter of the cleartext would map t
    # a letter between A and O. Which letter that is is also randomly
    # selected. This means it is entirely possible that the cipher text 
    # might still consist of fewer letters than the random number generated. 
    global cleartext
    global cipher
    global decrypt
    global alphaclear
    cipher = []         # clear routine should clean these but just in case
    decrypt = []        # clear routine should clean these but just in case
    cleartext=cleartext.upper()
    # get random number between 1 and 25 to denote range of scramble text letters
    dimension_size = random.randint(1, 25)
    
    cipher_range = alphaclear[0:dimension_size]

    # For each letter of the alphabet, create a mapping based on an index number
    # also save the index number because we build the decryption key from this
    for i in range (len(alphaclear)):
       key = random.randint(0, (len(cipher_range)-1))
       cipher.append(cipher_range[key])
       decrypt.append(key)
    
                     
    
def encrypt_text():
    global cleartext
    global cipher
    global crypttext
    global alphaclear

    # in this I learn that like assembler, this is a handy string
    # translate instruction. Here goes

    stringclear = ''.join(alphaclear)
    stringcipher = ''.join(cipher)
    translate_table = str.maketrans(stringclear,stringcipher)
    crypttext = cleartext.translate(translate_table)

def build_output():
    # ultimate objective here is to output to a file. 
    global crypttext
    global deconstruction
    print(crypttext)
    print(deconstruct)

def clear_keys_and_crypt():
    # these fields are used every time the encryption algorithm is run
    # so we should ensure they are clear at the start every time. 
    crypttext = ""
    deconstruct = ""
    cipher = []
    decrypt = []

def convert_text_upper():
    # made this easy by only using uppercase letters. 
    global cleartext
    cleartext = cleartext.upper()

# mainline processing

def main():
    global proceed
    print('Novel writing started at: ')
    print("Prologue")
    print(cleartext)
    print(datetime.datetime.now().time())
    convert_text_upper()

    #do 50 times
    # change this to 50 when finished testing
    for i in range(1,51):
        print("\n\n\nCHAPTER ",i)
        print("\n\n\n")
        create_encryption_key()
        encrypt_text()
        create_key()
        build_output()

        clear_keys_and_crypt()
    
    print(datetime.datetime.now().time())
    print("Encryption: A Novel - complete")


if __name__ == "__main__":
    main()

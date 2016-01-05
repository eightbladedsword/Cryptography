# Date: January 4, 2016
# Author: Joshua Janes
# A simple program that analyzes a text file for character frequency. Useful for
# decoding simple ciphertexts. Feel free to use this code however you like.

def main():
    try:
        file_name = \
            input("Enter the name of a .txt file you would like to analyze: ")
        open_file = open(file_name, "r")
    except IOError:
        print("No such file (maybe your file isn't in the current directory)")
        return
    
    alphabet_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text_size = 0
    char_count = [0] * 26
    
    while True:
        char = open_file.read(1).upper()
        if not char:
            break
        if char.isalpha():
            text_size += 1
            if char == "A":
                char_count[0] += 1
            elif char == 'B':
                char_count[1] += 1
            elif char == "C":
                char_count[2] += 1            
            elif char == "D":    
                char_count[3] += 1
            elif char == "E":
                char_count[4] += 1
            elif char == "F":
                char_count[5] += 1 
            elif char == "G":
                char_count[6] += 1
            elif char == "H":
                char_count[7] += 1            
            elif char == "I":    
                char_count[8] += 1
            elif char == "J":
                char_count[9] += 1
            elif char == "K":
                char_count[10] += 1                       
            elif char == "L":
                char_count[11] += 1            
            elif char == "M":    
                char_count[12] += 1
            elif char == "N":
                char_count[13] += 1
            elif char == "O":
                char_count[14] += 1 
            elif char == "P":
                char_count[15] += 1
            elif char == "Q":
                char_count[16] += 1            
            elif char == "R":    
                char_count[17] += 1
            elif char == "S":
                char_count[18] += 1
            elif char == "T":
                char_count[19] += 1 
            elif char == "U":
                char_count[20] += 1 
            elif char == "V":
                char_count[21] += 1
            elif char == "W":
                char_count[22] += 1            
            elif char == "X":    
                char_count[23] += 1
            elif char == "Y":
                char_count[24] += 1
            elif char == "Z":
                char_count[25] += 1             
       
    for i in range (0, 25):
        print("%s has a frequency of %.2f and occued %d times." \
              % (alphabet_string[i], char_count[i]/text_size, char_count[i]) )
    print("%s has a total of %d alphabetic characters."\
          % (file_name, text_size) )
main()   
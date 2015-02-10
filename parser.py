# Simple Data Parser for Data in Files
# I created this to read a text file and grab specific data I want from each line
# In particular each line of data contains a bunch of text, and the data I want is enclosed in Parentheses
# Assumes that each line is properly formatted (no safety checks)

# Imports
import os

# Gets input and determines name of output file to the original file name concatenated with _new
# e.g. If my input is file.txt then the output is file is file_new.txt
original_file_name = input('Enter file name (make sure the file is in same path): ')
original_file_name, original_file_ext = os.path.splitext(original_file_name)
new_file_name = original_file_name + "_new" + original_file_ext

# Open the files for writing and reading (these are different files)
with open (original_file_name + original_file_ext, 'r') as read_file:
    with open(new_file_name, 'w') as write_file:

        # Algorithm for Parsing
        # Reads original file line by line
        # Scans each line character by character until reaching first parenthesis 
        # Then reads characters and concatenates as a string until reading a closing parenthesis
        # The string is then written on a line in the new file
        for line in read_file:
            print(line)
         
            # Initialize counter index to 0, save flag to 0
            i = 0
            save = 0
            # Create Empty String
            temp_string = ""
            for i in range (0, len(line)):
                if line[i] == '(':
                    save = 1
                elif line[i] == ')':
                    break
                elif save == 1:
                    temp_string+=line[i]
              
            # Write word
            print(temp_string + '\n')
            write_file.write(temp_string+'\n')
         

print('Parser completed.')

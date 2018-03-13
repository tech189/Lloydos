import re

with open("test.ld", mode="r") as file:
    line_number = 0
    for line in file:
        line_number += 1
        if line[0] == "ὁ":
            print("Variable statement on line " + str(line_number)) #assuming we won't have variables in other genders
            if line[1:17] == " λογος ὀνομαζων ":
                print("String statement on line " + str(line_number))
                string_name = re.search("«(.*)» ", line[17:]).group(1)
                #print("String name is \"" + string_name + "\"")
                string_var = re.search("ι «(.*)»;", line[17:]).group(1)
                print("String statement equates \"" + string_name + "\" as \"" + string_var + "\"")
                #save string_name and string_var to a dictionary
            else:
                print("Syntax error on line " + str(line_number))
        elif line[0:5] == "εἰπε ":
            print("Print statement on line " + str(line_number))
            #retrieve from dictionary the string and print it!
        else:
            print("Sytax error on line " + str(line_number))
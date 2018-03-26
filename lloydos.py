import re

with open("test.ld", mode="r") as file:
    line_number = 0
    strings = {}
    numbers = {}
    for line in file:
        line_number += 1
        if line[0] == "#":
            print("Comment on line " + str(line_number))
        elif line[0] == "ὁ":
            #print("Variable statement on line " + str(line_number)) #assuming we won't have variables in other genders
            if line[1:17] == " λογος ὀνομαζων ":
                #print("String statement on line " + str(line_number))
                string_name = re.search("«(.*)» ", line[17:]).group(1)
                string_var = re.search("ι «(.*)»;", line[17:]).group(1)
                #print("String statement equates \"" + string_name + "\" as \"" + string_var + "\"")
                #save string_name and string_var to a dictionary
                strings[string_name] = string_var
            elif line[1:19] == " ἀριθμος ὀνομαζων ":
                #print("String statement on line " + str(line_number))
                number_name = re.search("«(.*)» ", line[17:]).group(1)
                number_var = re.search("ι «(.*)»;", line[17:]).group(1)
                #print("String statement equates \"" + string_name + "\" as \"" + string_var + "\"")
                #save string_name and string_var to a dictionary
                numbers[number_name] = number_var
            else:
                print("Syntax error on line " + str(line_number))
        elif line[0:5] == "εἰπε ":
            #print("Print statement on line " + str(line_number))
            #retrieve from dictionary the string and print it!
            if line[5:26] == "τον λογον ὀνομαζοντα ":
                string_name = re.search("«(.*)»;", line[26:]).group(1)
                print(strings[string_name])
            elif line[5:26] == "τον ἀριθμον ὀνομαζοντα ":
                #how do you print numbers???????????????????????????????????????/?????????????????
                number_name = re.search("«(.*)»;", line[26:]).group(1)
                print(numbers[number_name])
        elif line[0:5] == "λεγε ":
            #print("Infinite print statement on line " + str(line_number))
            #retrieve from dictionary the string and print it!
            if line[5:26] == "τον λογον ὀνομαζοντα ":
                string_name = re.search("«(.*)»;", line[26:]).group(1)
                while True:
                    print(strings[string_name])
        else:
            print("Sytax error on line " + str(line_number))
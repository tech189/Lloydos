import re, math

#can't go higher than 999
numerals = {
    "0": "οὐδεν",
    "1": "α",
    "2": "β",
    "3": "γ",
    "π": math.pi,
    "4": "δ",
    "5": "ε",
    "6": "ϝ",
    "7": "ζ",
    "8": "η",
    "9": "θ",
    "g": "9.81",
    "10": "ι",
    "20": "κ",
    "30": "λ",
    "40": "μ",
    "50": "ν",
    "60": "ξ",
    "70": "ο",
    "80": "π",
    "90": "ϙ",
    "100": "ρ",
    "200": "σ",
    "300": "τ",
    "400": "υ",
    "500": "φ",
    "600": "χ",
    "700": "ψ",
    "800": "ω",
    "900": "Ͳ",
    #"Ϡ": marker for 1000 so maybe Ϡα = 1000?
    "c": 299792458
}

with open("test.ld", mode="r") as file:
    line_number = 0
    strings = {}
    numbers = {}
    for line in file:
        line_number += 1
        #print("DEBUG: Line " + line_number + " is --" + line + "--")
        if line == "\n":
            continue
            #print("DEBUG: Empty line on line " + str(line_number))
        elif line[0] == "#":
            continue
            #print("DEBUG: Comment on line " + str(line_number))
        elif line[0] == "ὁ":
            #print("DEBUG: Variable statement on line " + str(line_number)) #assuming we won't have variables in other genders
            if line[1:17] == " λογος ὀνομαζων ":
                #print("DEBUG: String statement on line " + str(line_number))
                string_name = re.search("«(.*)» ", line[17:]).group(1)
                string_var = re.search("ι «(.*)»;", line[17:]).group(1)
                #print("DEBUG: String statement equates \"" + string_name + "\" as \"" + string_var + "\"")
                #save string_name and string_var to a dictionary
                strings[string_name] = string_var
            elif line[1:19] == " ἀριθμος ὀνομαζων ":
                #print("DEBUG: String statement on line " + str(line_number))
                number_name = re.search("«(.*)» ", line[17:]).group(1)
                number_var = re.search("ι «(.*)»;", line[17:]).group(1)
               #print("DEBUG: Number statement equates \"" + number_name + "\" to the value " + number_var + "")
                #save string_name and string_var to a dictionary
                numbers[number_name] = number_var
            else:
                print("Syntax error on line " + str(line_number))
        elif line[0:5] == "εἰπε ":
            #print("DEBUG: Print statement on line " + str(line_number))
            #retrieve from dictionary the string and print it!
            #print("-"+line[5:28]+"-")
            if line[5:26] == "τον λογον ὀνομαζοντα ":
                string_name = re.search("«(.*)»;", line[26:]).group(1)
                print(strings[string_name])
            elif line[5:28] == "τον ἀριθμον ὀνομαζοντα ":
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
            print("ERROR: Sytax error on line " + str(line_number))
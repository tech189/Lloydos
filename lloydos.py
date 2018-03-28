import re, math, sys, logging

help_text = "aldfj"

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

def run_code(file_name, options):
    if "-d" in options:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug(" Command line options: " + str(options))
    with open(file_name, mode="r") as file:
        line_number = 0
        strings = {}
        numbers = {}
        for line in file:
            line_number += 1
            #logging.debug(" Line " + str(line_number) + " is --" + line + "--")
            if line == "\n":
                logging.debug(" Empty line on line " + str(line_number))
                continue
            elif line[0] == "#":
                logging.debug(" Comment on line " + str(line_number))
                continue
            elif line[0] == "ὁ":
                logging.debug(" Variable statement on line " + str(line_number)) #assuming we won't have variables in other genders
                if line[1:17] == " λογος ὀνομαζων ":
                    logging.debug(" String statement on line " + str(line_number))
                    string_name = re.search("«(.*)» ", line[17:]).group(1)
                    string_var = re.search("ι «(.*)»;", line[17:]).group(1)
                    logging.debug(" String statement equates \"" + string_name + "\" as \"" + string_var + "\"")
                    #save string_name and string_var to a dictionary
                    strings[string_name] = string_var
                elif line[1:19] == " ἀριθμος ὀνομαζων ":
                    logging.debug(" Number statement on line " + str(line_number))
                    number_name = re.search("«(.*)» ", line[17:]).group(1)
                    if re.search("ι «(.*)»;", line[17:]).group(1).isdigit() == False:
                        print("DEBUG: Not a digit, variable not created")
                    else:
                        number_var = re.search("ι «(.*)»;", line[17:]).group(1)
                        numbers[number_name] = number_var
                    logging.debug(" Number statement equates \"" + number_name + "\" to the value " + number_var + "")
                    #save string_name and string_var to a dictionary
                else:
                    print("Syntax error on line " + str(line_number))
            elif line[0:5] == "εἰπε ":
                logging.debug(" Print statement on line " + str(line_number))
                #retrieve from dictionary the string and print it!
                #print("-"+line[5:28]+"-")
                if line[5:26] == "τον λογον ὀνομαζοντα ":
                    string_name = re.search("«(.*)»;", line[26:]).group(1)
                    try:
                        print(strings[string_name])
                    except KeyError:
                        logging.error(" No such string variable as «" + string_name + "»")
                elif line[5:28] == "τον ἀριθμον ὀνομαζοντα ":
                    number_name = re.search("«(.*)»;", line[26:]).group(1)
                    try:
                        print(numbers[number_name])
                    except KeyError:
                        logging.error(" No such number variable as «" + number_name + "» (line " + str(line_number) + ")")
            elif line[0:5] == "λεγε ":
                #print("Infinite print statement on line " + str(line_number))
                #retrieve from dictionary the string and print it!
                if line[5:26] == "τον λογον ὀνομαζοντα ":
                    string_name = re.search("«(.*)»;", line[26:]).group(1)
                    try:
                        print(strings[string_name])
                        while True:
                            try:
                                print(strings[string_name])
                            except KeyboardInterrupt:
                                logging.info(" Infinite print statement stopped")
                                exit()
                    except KeyError:
                        logging.error(" No such string variable as «" + string_name + "» (line " + str(line_number) + ")")
                elif line[5:28] == "τον ἀριθμον ὀνομαζοντα ":
                    number_name = re.search("«(.*)»;", line[17:]).group(1)
                    try:
                        print(numbers[number_name])
                        while True:
                            try:
                                print(numbers[number_name])
                            except KeyboardInterrupt:
                                logging.info(" Infinite print statement stopped")
                                exit()
                    except KeyError:
                        logging.error("  No such number variable as «" + number_name + "» (line " + str(line_number) + ")")
            else:
                logging.error("  Sytax error on line " + str(line_number))
    logging.debug(" Number variables: " + str(numbers))
    logging.debug(" String variables: " + str(strings))

if len(sys.argv) < 2:
    print(help_text)
elif len(sys.argv) == 2:
    try:
        run_code(sys.argv[1], [])
        logging.getLogger().setLevel(logging.INFO)
    except FileNotFoundError:
        print("Input file \"" + sys.argv[1] + "\" does not exist")
elif len(sys.argv) > 2:
    try:
        run_code(sys.argv[1], sys.argv[2:])
    except FileNotFoundError:
        print("Input file \"" + sys.argv[1] + "\" does not exist")
else:
    print(help_text)
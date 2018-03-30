import re, sys, logging

help_text = "Sytax:\n\tlloydos [filename] [options]\nOptions:\n\t-d\tDebug mode\tExtra information is printed"

#can't go higher than 999
numerals = {
    "οὐδεν": 0,
    "α": 1,
    "β": 2,
    "γ": 3,
    "δ": 4,
    "ε": 5,
    "ϝ": 6,
    "ζ": 7,
    "η": 8,
    "θ": 9,
    "ι": 10,
    "κ": 20,
    "λ": 30,
    "μ": 40,
    "ν": 50,
    "ξ": 60,
    "ο": 70,
    "π": 80,
    "ϙ": 90,
    "ρ": 100,
    "σ": 200,
    "τ": 300,
    "υ": 400,
    "φ": 500,
    "χ": 600,
    "ψ": 700,
    "ω": 800,
    "Ͳ": 900
    #"Ϡ": marker for 1000 so maybe Ϡα = 1000?
    #"g": 9.81
    #"c": 299792458
}

def run_code(file_name, options):
    if "-d" in options:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug(" Command line options: " + str(options))
    with open(file_name, mode="r", encoding="utf8") as file:
        line_number = 0
        strings = {}
        numbers = {}
        for line in file:
            line_number += 1
            #logging.debug(" Line " + str(line_number) + " is «" + line + "»")
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
                        logging.debug(" Not a digit, variable not created")
                        try:
                            input = re.search("ι «(.*)ʹ»;", line[17:]).group(1)
                            number = 0
                            for i in input:
                                if i in numerals:
                                    number = number + numerals[i]
                            numbers[number_name] = number
                        except AttributeError:
                            logging.error(" Syntax error on line " + str(line_number) +  ": entering numerals (use a ʹ)")
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
                        logging.error(" No such number variable as «" + number_name + "» (line " + str(line_number) + ")")
            else:
                logging.error(" Sytax error on line " + str(line_number))
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
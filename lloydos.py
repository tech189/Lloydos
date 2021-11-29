# resources:
# http://lisperator.net/pltut/
# https://medium.freecodecamp.org/the-programming-language-pipeline-91d3f449c919
# https://tomassetti.me/resources-create-programming-languages/#parsing-tutorials

import re, sys, logging
import argparse

help_text = "Usage:\n\tlloydos.py [filename] [options]\nOptions:\n\t-d\tDebug mode\tdisplays a lot of detailed information about each line of code"

#can't go higher than 999
numerals = {
    #"οὐδεν": 0,
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

logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter("%(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def run_code(file_name):
    with open(file_name, mode="r", encoding="utf8") as file:
        line_number = 0
        strings = {}
        numbers = {}
        for line in file:
            line_number += 1
            #logger.debug("Line " + str(line_number) + " is «" + line + "»")
            if line == "\n":
                logger.debug("Empty line on line " + str(line_number))
                continue
            elif line[0] == "#":
                logger.debug("Comment on line " + str(line_number))
                continue
            elif line[0] == "ὁ":
                logger.debug("Variable statement on line " + str(line_number)) #assuming we won't have variables in other genders
                if line[1:17] == " λογος ὀνομαζων ":
                    logger.debug("String statement on line " + str(line_number))
                    string_name = re.search("«(.*)» ", line[17:]).group(1)
                    string_var = re.search("ι «(.*)»;", line[17:]).group(1)
                    logger.debug("String statement equates \"" + string_name + "\" as \"" + string_var + "\"")
                    #save string_name and string_var to a dictionary
                    strings[string_name] = string_var
                elif line[1:19] == " ἀριθμος ὀνομαζων ":
                    logger.debug("Number statement on line " + str(line_number))
                    number_name = re.search("«(.*)» ", line[17:]).group(1)
                    #print(str(re.search("ι «(.*)»;", line[17:]).group(1).isdigit()) + "line" + str(line_number))
                    if re.search("ι «(.*)»;", line[17:]).group(1).isdigit() == False:
                        try:
                            input = re.search("ι «(.*)ʹ»;", line[17:]).group(1)
                            number = 0
                            #print("input is " + input)
                            there_are_numerals = 0
                            for i in input:
                                if i in numerals:
                                    logger.debug("Greek numerals found")
                                elif i not in numerals:
                                    logger.error("Not a Greek numeral, no assignment made (line " + str(line_number) + ")")
                                    there_are_numerals = False
                                    break
                            if there_are_numerals is False:
                                #print("ok so there are no numerals")
                                continue
                            else:
                                for i in input:
                                    if i in numerals:
                                        number = number + numerals[i]
                                numbers[number_name] = number
                        except AttributeError:
                            logger.error("Syntax error on line " + str(line_number) +  ": entering numerals (use a ʹ)")
                    else:
                        number_var = re.search("ι «(.*)»;", line[17:]).group(1)
                        numbers[number_name] = number_var
                        # TODO why does this debug never run?
                        logger.debug("Number statement equates \"" + number_name + "\" to the value " + number_var + "")
                    #save string_name and string_var to a dictionary
                else:
                    print("Syntax error on line " + str(line_number))
            elif line[0:5] == "εἰπε ":
                logger.debug("Print statement on line " + str(line_number))
                #retrieve from dictionary the string and print it!
                #print("-"+line[5:28]+"-")
                if line[5:26] == "τον λογον ὀνομαζοντα ":
                    string_name = re.search("«(.*)»;", line[26:]).group(1)
                    try:
                        print(strings[string_name])
                    except KeyError:
                        logger.error("No such string variable as «" + string_name + "»")
                elif line[5:28] == "τον ἀριθμον ὀνομαζοντα ":
                    number_name = re.search("«(.*)»;", line[26:]).group(1)
                    try:
                        print(numbers[number_name])
                    except KeyError:
                        logger.error("No such number variable as «" + number_name + "» (line " + str(line_number) + ")")
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
                                logger.info("Infinite print statement stopped")
                                exit()
                    except KeyError:
                        logger.error("No such string variable as «" + string_name + "» (line " + str(line_number) + ")")
                elif line[5:28] == "τον ἀριθμον ὀνομαζοντα ":
                    number_name = re.search("«(.*)»;", line[17:]).group(1)
                    try:
                        print(numbers[number_name])
                        while True:
                            try:
                                print(numbers[number_name])
                            except KeyboardInterrupt:
                                logger.info("Infinite print statement stopped")
                                exit()
                    except KeyError:
                        logger.error("No such number variable as «" + number_name + "» (line " + str(line_number) + ")")
            else:
                logger.error("Sytax error on line " + str(line_number))
    logger.debug("Number variables: " + str(numbers))
    logger.debug("String variables: " + str(strings))

# # TODO replace with argparse
# if len(sys.argv) < 2:
#     print(help_text)
# elif len(sys.argv) == 2:
#     try:
#         run_code(sys.argv[1], [])
#         logging.getLogger().setLevel(logging.INFO)
#     except FileNotFoundError:
#         print("Input file \"" + sys.argv[1] + "\" does not exist")
# elif len(sys.argv) > 2:
#     try:
#         run_code(sys.argv[1], sys.argv[2:])
#     except FileNotFoundError:
#         print("Input file \"" + sys.argv[1] + "\" does not exist")
# else:
#     print(help_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interprets files written in the esoteric programming language Lloydos")
    parser.add_argument("file")
    parser.add_argument("--debug", help="print calculations etc. for debugging", action="store_true")
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)
    
    try:
        run_code(args.file)
    except FileNotFoundError:
        logger.error("Input file \"" + args.file + "\" does not exist")
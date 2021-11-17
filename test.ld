# testing assigning string variables and printing them
ὁ λογος ὀνομαζων «hello» ἐστι «Hello, world!»;
εἰπε τον λογον ὀνομαζοντα «hello»;

ὁ λογος ὀνομαζων «hello» ἐστι «Hello, tech189!»;
εἰπε τον λογον ὀνομαζοντα «hello»;

ὁ λογος ὀνομαζων «test» ἐστι «Test test test»;
εἰπε τον λογον ὀνομαζοντα «test»;

# testing assigning an integer variable and printing it
ὁ ἀριθμος ὀνομαζων «number» ἐστι «σμαʹ»;
εἰπε τον ἀριθμον ὀνομαζοντα «number»;

# assignment fails because arabic numerals used, variable unchanged
ὁ ἀριθμος ὀνομαζων «number» ἐστι «1ʹ»;
εἰπε τον ἀριθμον ὀνομαζοντα «number»;

# assignment fails again, variable unchanged
ὁ ἀριθμος ὀνομαζων «number» ἐστι «ae21ʹ»;
εἰπε τον ἀριθμον ὀνομαζοντα «number»;

# testing assigning highest number - 999
ὁ ἀριθμος ὀνομαζων «other number» ἐστι «Ͳϙθʹ»;
εἰπε τον ἀριθμον ὀνομαζοντα «other number»;

# infinite loop left commented out
# λεγε τον λογον ὀνομαζοντα «hello»;

# while loop - unimplemented
# του ἀριθμος ὀνομαζοντος «number» αὐξανοντος και ὁ ἀριθμος ἐστι ἡσσων «5»·
#     εἰπε τον λογον ὀνομαζοντα «hello»;
#     εἰπε τον ἀριθμον ὀνομαζοντα «number»;

# if uncommented, this line should raise a syntax error
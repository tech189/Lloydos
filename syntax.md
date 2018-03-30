Syntax
========

Variables
---------

### __Strings__

    ὁ λογος ὀνομαζων «hello» ἐστι «Hello, world!»;

Translation: The word/phrase being called `«varname»` is `«string»`

### __Numbers__

    ὁ ἀριθμος ὀνομαζων «number» ἐστι «0»;

Translation: The number being called `«varname»` is `«integer»`

Comments
--------

    #this is a one line comment

It is not possible to write in-line comments yet.

    #this is how you
    #do multiple lines

Commands
--------

### __Print statements__

    εἰπε τον λογον ὀνομαζοντα «hello»;

Translation: Say (once) the phrase being called `«varname»`

    εἰπε τον ἀριθμον ὀνομαζοντα «number»;

Translation: Say (once) the number being called `«varname»`

### __Infinite print statements__

    λεγε τον λογον ὀνομαζοντα «hello»;

Translation: Say (repeatedly) the phrase being called `«varname»`

    λεγε τον ἀριθμον ὀνομαζοντα «number»;

Translation: Say (repeatedly) the number being called `«varname»`

Loops
-----

### While loops

*__NOT YET IMPLEMENTED__*


    του ἀριθμος ὀνομαζοντος «number» αὐξανοντος και ὁ ἀριθμος ἐστι ἡσσων «5»·
        εἰπε τον λογον ὀνομαζοντα «hello»;
        εἰπε τον ἀριθμον ὀνομαζοντα «number»;

Translation: while the number being called `«varname»` is increasing and the number is less than `«integer»` (· is effectively a semicolon; then do the following indented lines)

- increasing = `αὐξανοντος`
- decreasing = `μειωνοντος`
- less than = `ἡσσων`
- greater than = `μειζων`
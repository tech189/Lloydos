# Syntax

#### NB: 
- Use UTF-8 encoding in your files!
- The semicolon looking thing at the end of each line is actually a Greek question mark!
- Don't forget your breathings
- Use `«` and `»` instead of quotation marks

## Variables


### __Strings__

    ὁ λογος ὀνομαζων «hello» ἐστι «Hello, world!»;

Translation: The word/phrase being called `«varname»` is `«string»`

### __Numbers__

    ὁ ἀριθμος ὀνομαζων «number» ἐστι «0»;

Translation: The number being called `«varname»` is `«integer»`

You can also use [Greek numerals](https://en.wikipedia.org/wiki/Greek_numerals#Table) (up to 999 at the moment) in your variables:

    ὁ ἀριθμος ὀνομαζων «number» ἐστι «σμαʹ»;
    #This is stored as 241

| Western Arabic   | Ancient Greek |
|------------------|---------------|
| 1                | α             |
| 2                | β             |
| 3                | γ             |
| 4                | δ             |
| 5                | ε             |
| 6                | ϝ             |
| 7                | ζ             |
| 8                | η             |
| 9                | θ             |
| 10               | ι             |
| 20               | κ             |
| 30               | λ             |
| 40               | μ             |
| 50               | ν             |
| 60               | ξ             |
| 70               | ο             |
| 80               | π             |
| 90               | ϙ             |
| 100              | ρ             |
| 200              | σ             |
| 300              | τ             |
| 400              | υ             |
| 500              | φ             |
| 600              | χ             |
| 700              | ψ             |
| 800              | ω             |
| 900              | Ͳ             |

## Comments

    #this is a one line comment

It is not possible to write in-line comments yet.

    #this is how you
    #do multiple lines

## Commands


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

## Loops

### While loops

*__NOT YET IMPLEMENTED__*


    του ἀριθμος ὀνομαζοντος «number» αὐξανοντος και ὁ ἀριθμος ἐστι ἡσσων «5»·
        εἰπε τον λογον ὀνομαζοντα «hello»;
        εἰπε τον ἀριθμον ὀνομαζοντα «number»;

Translation: while the number being called `«varname»` is increasing and the number is less than `«integer»` (`·` is effectively a semicolon; then do the following indented lines)

- increasing = `αὐξανοντος`
- decreasing = `μειωνοντος`
- less than = `ἡσσων`
- greater than = `μειζων`

## If statements

*__NOT YET IMPLEMENTED__*

    εἰ ὁ λογος ὀνομαζων «hello» ἐστι «Hello, world!»·
        εἰπε τον ἀριθμον ὀνομαζοντα «number»;
    εἰ μη·
        εἰπε τον ἀριθμον ὀνομαζοντα «other number»;

Translation: if the word being called `«varname»` is `«value»` (`·` is effectively a semicolon; then do the following indented lines) if not (`·` = do the following)

- less than = `ἡσσων`
- greater than = `μειζων`
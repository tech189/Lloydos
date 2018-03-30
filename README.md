# Lloydos

### TL;DR: An esoteric programming language written in Ancient Greek

## Interpreter

Currently it is just an interpreter written in Python 3 that takes in `.ld` files.

## Example

Here we have a file called `test.ld` with the following inside:

    ὁ λογος ὀνομαζων «hello» ἐστι «Hello, world!»;
    εἰπε τον λογον ὀνομαζοντα «hello»;

    ὁ λογος ὀνομαζων «hello» ἐστι «Hello, tech189!»;
    εἰπε τον λογον ὀνομαζοντα «hello»;

    ὁ ἀριθμος ὀνομαζων «number» ἐστι «7»;
    εἰπε τον ἀριθμον ὀνομαζοντα «number»;

    ὁ ἀριθμος ὀνομαζων «other number» ἐστι «Ͳϙθʹ»;
    εἰπε τον ἀριθμον ὀνομαζοντα «other number»;

And then we run the following:

    D:\Coding\Python\Lloydos>python lloydos.py test.ld

We should get this output:

    Hello, world!
    Hello, tech189!
    7
    999

## Syntax

It is fairly basic at the moment but all of the relevant documentation is in [syntax.md](syntax.md)

## Options

Usage:

    lloydos.py [filename] [options]

- `-d` Debug mode - displays a lot of detailed information about each line of code

## Progress

Check out the progress of the project [here](https://github.com/tech189/Lloydos/projects/1) and submit any issues [here](https://github.com/tech189/Lloydos/issues).
#! /usr/bin/python3

# Fully Dual intuitionistic sequent calculus in python

# I would have preferred to use another language, but python is the prototyping
# language I know the best and is the easiest to write a parser with


# lexers need to read by char, not by line
def chars(iostream):
    for line in iostream:
        for c in line:
            yield c
        yield "\n"


# Helper decorator for coroutines
def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start


# Python coroutine lexer, because, well, coroutines are cool.
def lex(iostream, parser):
    mode = lex_main(parser)
    for c in chars(iostream):
        mode = mode.send(c)

@coroutine
def lex_main(parser):
    c = (yield)
    while c is not None:
        if c is "#":
            yield lex_comment(parser)
        elif c in "\"'":
            yield lex_quoted(c, parser)
        elif c in " \n\t":
            pass
        elif c.isalnum():
            lm = lex_atom(parser)
            lm.send(c)
            yield lm
        else:
            lm = lex_op(parser)
            lm.send(c)
            yield lm
        c = (yield)

@coroutine
def lex_comment(parser):
    c = (yield)
    while c is not "\n":
        pass
    yield lex_main(parser)

@coroutine
def lex_quoted(quotechar, parser):
    c = (yield)
    term = c
    while c is not quotechar or term[-1] is "\\":
        term += c
        c = (yield)
    parser.send(("string", term) if quotechar is "\"" else ("atom", term))
    yield lex_main(parser)

@coroutine
def lex_atom(parser):
    c = (yield)
    term = c
    while c.isalnum():
        term += c
        c = (yield)
    parser.send(("atom", term))
    lm = lexer_main(parser)
    lm.send(c)
    yield lm

@coroutine
def lex_op(parser):
    c = (yield)
    lm = lexer_main(parser)
    if c is "-":
        term = c+(yield)
        if term is "->" or term is "-<":
            parser.send(("op", term))
        else:
            parser.send(("op", c))
            lm.send(term[-1])
    else:
        parser.send(("op", c))
    yield lm

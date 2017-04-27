%% Implementation of declarative sets in prolog via red-black trees

%% Prolog's default set implementation is based on lists and not very
%% declarative. I want to be able to talk about sets like lists, induce on them
%% and so on.

:- module(set, [null/0, in/2, U/2, I/2, =/2, =</2]).

:- op(700, xfx, in).
:- op(500, yfx, U).
:- op(500, yfx, I).

in(X, S) :- member(X, S).
in((X,Xs), S) :- member(X, S), in(Xs, S).

member(X, set(S)) :- member(X, S).
member(X, black(X, _, _)).
member(X, red(X, _, _)).
member(X, black(Y, L, R)) :- \+ X = Y,
    term_string(X, SX), term_string(Y, SY),
    (SX < SY ->
        member(X, L)
    ;
        member(X, R)
    ).

null :- black(leaf).


directlyIn(olga, katarina).
directlyIn(natasha, olga).
directlyIn(irina, natasha).

contains(X, Y) :-
    directlyIn(Y, X).
contains(X, Y) :-
    directlyIn(Y, Z),
    contains(X, Z).


test_answer0 :-
    directlyIn(irina, natasha),
    writeln('OK').

test_answer1 :-
    \+ directlyIn(irina, olga),
    writeln('OK').

test_answer2 :-
    contains(katarina, irina),
    writeln('OK').

test_answer3 :-
    contains(katarina, natasha),
    writeln('OK').

% Here we look for all of the dolls which contain irina.

test_answer4 :-
    findall(P, contains(P, irina), Output),
    sort(Output, SortedOutput),
    foreach(member(X,SortedOutput), (write(X), nl)).

directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).

contains(X, Y) :- directlyIn(Y, X).
contains(X, Y) :- directlyIn(Z, X), contains(Z, Y).

test_answer :-
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

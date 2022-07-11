remove(_,[],[]).
remove(X, [X|T1],T2):- remove(X, T1, T2).
remove(X, [H1|T1], [H1|T2]):- X \= H1, remove(X, T1, T2).

test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    writeln(L).

test_answer1 :-
    remove(2, [2], L),
    writeln(L).

test_answer2 :-
    remove(d, [a, b, c], L),
    write(L).

test_answer3 :-
    remove(a, [], L),
    write(L).

test_answer4 :-
    remove(term2, [term1, term2, term3], [term1, term3]),
    write('OK').

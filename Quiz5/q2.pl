swap12([H1|T1], [H2|T2]) :- compare(T2, H1), compare(T1, H2), list_compare(T1, T2).
compare([H|T], X) :- X = H.
list_compare([H1|T1], [H2|T2]) :- T1 = T2.

test_answer0 :-
    swap12([a, b, c, d], L),
    writeln(L).

test_answer1 :-
    \+ swap12(L, [1]),
    writeln('OK').

test_answer2 :-
  swap12(L, [b, a]),
  writeln(L).

test_answer3 :-
    swap12(L1, L2),
    writeln('OK').

swap12([H1,S1|T1], [H2,S2|T2]) :- T1 = T2, H1 = S2, S1 = H2.

test_answer :-
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

swap12([A,B|T], [B,A|T]).

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

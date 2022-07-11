asbs([]).
asbs([H|T]) :- H = a, asbs(T); H=b, bs(T).
bs([]).
bs([H|T]) :- H = b, bs(T).

test_answer :-
    asbs([a,a,a,b]),
    writeln('OK').
test_answer1 :-
    \+ asbs([a,b,a]),
    writeln('OK').

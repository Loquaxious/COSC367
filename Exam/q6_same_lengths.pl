same_evens([]).
same_evens([H1, H2|T]) :- move(H2, T).
move(_,[]).
move(X, [H1, X | T]) :- move(X, T).


test_answer :-
    same_evens([a, b, c, b, d, b]),
    same_evens([a, b]),
    same_evens([]),
    writeln('OK').

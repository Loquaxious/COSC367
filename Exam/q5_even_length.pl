even_length([]).
even_length([H|T]) :- even(T).
even([H|T]) :- even_length(T).


test_answer :-
    even_length([foo, bar, zoo, log]),
    writeln('OK').
test_answer1 :-
    \+ even_length([1]),
    \+ even_length(this_is_not_a_list),
    writeln('OK').

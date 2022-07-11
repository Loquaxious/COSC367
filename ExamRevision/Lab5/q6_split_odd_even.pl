split_odd_even([], [], []).
even([],[],[]).
split_odd_even([H|T], [H|O], E) :- even(T, O, E).
even([H|T], O, [H|E]) :- split_odd_even(T, O, E).

test_answer :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    writeln(B).

test_answer1 :-
    split_odd_even([1,2,3,5], A, B),
    write(A),
    writeln(B).

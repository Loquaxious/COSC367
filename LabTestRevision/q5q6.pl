split_odd_even([], [], []).
even([],[],[]).
split_odd_even([HI|TI], [HI|TA], TB):- even(TI, TA, TB).
even([HI|TI], TA, [HI|TB]) :- split_odd_even(TI, TA, TB).

test_answer :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    writeln(B).

test_answer1 :-
    split_odd_even([1,2,3,5], A, B),
    write(A),
    writeln(B).

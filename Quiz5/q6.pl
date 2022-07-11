split_odd_even(Input, Odd, Even) :- split_odd(Input, Odd, Even).

split_odd([H1|T1],[H1|T2],X):- split_even(T1,T2,X).
split_odd([], [], []).

split_even([H1|T1],X,[H1|T3]):- split_odd(T1,X,T3).
split_even([],[],[]).

test_answer :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    writeln(B).

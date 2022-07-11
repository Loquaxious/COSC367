reversed([], []).
% alternatively you can write reversed(Forward, Backward):- Forward=[], Backward=[].

% Complete the following
reversed([Head|Tail], Backward) :- reversed(Tail,ReversedTail),
                                   append(ReversedTail, [Head], Backward).

test_answer :-
   reversed([1, 2, 3, 4, 5], L),
   writeln(L).

test_answer1 :-
   reversed(L, [d, c, b, a]),
   writeln(L).

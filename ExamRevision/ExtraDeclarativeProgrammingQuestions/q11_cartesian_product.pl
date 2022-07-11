% The following helper predicate multiplies a single element by a list
product(_, [], []).   % base case
product(X, [H|T], [(X, H) | MorePairs]) :- product(X, T, MorePairs). % Complete

cartesian_product([], _, []).
cartesian_product([Head|Tail], ListB, AllPairs) :-
    product(Head, ListB, HeadPairs),
    cartesian_product(Tail, ListB, RemainingPairs),  % Complete
    append(HeadPairs, RemainingPairs, AllPairs).  % Complete

test_answer :- cartesian_product([a, b], [1, 2], X),
               writeln(X).

test_answer1 :- cartesian_product([a, b], X, 
                                 [(a,1), (a,2), (b,1), (b,2)]),
               writeln(X).

unique([], []).
unique([H|T], S) :- member(H, T), unique(T, S).
unique([H|T], [H|S]) :- unique(T, S).

# unique([],[]).  % Complete the base case.
#
# % In the following we consider two cases: a) The head does not appear in the tail; b) it does.
#
# unique([H|T], [H|Set]) :-
#     \+ member(H, T),
#     unique(T, Set). % Complete
#
# unique([H|T], Set) :-
#     member(H, T), % Complete
#     unique(T, Set).   % Complete


test_answer :-
    unique([1,2,1,4,3,3], Set),
    sort(Set,Sorted),
    writeln(Sorted).

test_answer1 :-
    unique([], Set),
    sort(Set,Sorted),
    writeln(Sorted).

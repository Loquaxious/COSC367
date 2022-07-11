% See the lecture notes.
% Write the base case (complete the following)
new_append([] , B , B).

% Complete the following
new_append([X | Xs], B, [X|XsB]) :- new_append(Xs , B , XsB).

test_answer :-
    new_append([1, 2, 3], [a, b, c], L),
    writeln(L).

test_answer1 :-
    new_append([1, 2, 3], L, [1, 2, 3, 4, 5]),
    writeln(L).

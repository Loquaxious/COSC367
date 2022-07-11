merge([], ListB, ListB).   % Complete one of the two base cases
merge(ListA, [], ListA).    % Complete the other base case

merge([X | ListA], [Y | ListB], [X | Merged]) :-
    X < Y,
    merge(ListA, [Y | ListB], Merged).

merge([X | ListA], [Y | ListB], [Y | Merged]) :-   % Complete the other rule
    X >= Y,
    merge([X|ListA], ListB, Merged).

test_answer :-
  merge([3, 6, 7], [1, 2, 3, 5, 8], L),
  writeln(L).

test_answer1 :-
  merge([3, 6, 7], [], L),
  writeln(L).

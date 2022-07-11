% Write the rules for merge
% Write the rules for split_odd_even

merge_sort([], []).  % Complete base case for the empty list
merge_sort([X], [X]). % Complete the base for a list with only one element

merge_sort(List, Sorted):-
	List = [_,_|_],    % the list has two or more elements
	split_odd_even(List, SubSeq1, SubSeq2),  % create two subproblems (divide)
	merge_sort(SubSeq1, SortedSeq1), % Complete (solve)
	merge_sort(SubSeq2, SortedSeq2),  % Complete (solve)
	merge(SortedSeq1, SortedSeq2, Sorted).   % Complet (combine)

split_odd_even([], [], []).
even([],[],[]).
split_odd_even([H|T], [H|O], E) :- even(T, O, E).
even([H|T], O, [H|E]) :- split_odd_even(T, O, E).

merge([], ListB, ListB).   % Complete one of the two base cases
merge(ListA, [], ListA).    % Complete the other base case
merge([X | ListA], [Y | ListB], [X | Merged]) :-
    X < Y,
    merge(ListA, [Y | ListB], Merged).
merge([X | ListA], [Y | ListB], [Y | Merged]) :-   % Complete the other rule
    X >= Y,
    merge([X|ListA], ListB, Merged).

  test_answer :-
      merge_sort([4,3,1,2], L),
      writeln(L).

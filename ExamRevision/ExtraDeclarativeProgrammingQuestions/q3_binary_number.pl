# zero_or_one(D):- D = 0; D = 1.
# zero_or_one_sequence([H|T]) :- zero_or_one(H), (T=[]; zero_or_one_sequence(T)).
# binary_number([0, b | Ds]) :- zero_or_one_sequence(Ds).

% Instead of the first two clauses, a more verbose solution would be to write:
zero_or_one_sequence([0]).
zero_or_one_sequence([1]).
zero_or_one_sequence([0|Tail]) :- zero_or_one_sequence(Tail).
zero_or_one_sequence([1|Tail]) :- zero_or_one_sequence(Tail).
binary_number([0, b | Ds]) :- zero_or_one_sequence(Ds).

test_answer :- binary_number([0, b, 1, 0, 1]),
               writeln('OK').

test_answer1 :- binary_number([0, b, 0, 1, 2]),
               writeln('Wrong!'), halt.
test_answer1 :- writeln('OK').

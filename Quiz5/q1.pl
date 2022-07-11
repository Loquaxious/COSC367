compare([H|T], X) :- X = H.
second([H|T], X) :- compare(T, X).

test_answer0 :-
    second([cosc, 2, Var, beethoven], X),
    writeln(X).

  test_answer1 :-
      \+ second([1], X),
      writeln('OK').

  test_answer1 :-
      second([_],_),
      writeln('The predicate should fail on lists of length one!').

test_answer2 :-
    second([a, b, c, d], b),
    writeln('OK').

test_answer3 :-
    second(L, X),
    writeln('OK').

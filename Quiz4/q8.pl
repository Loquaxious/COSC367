mirror(leaf(X), leaf(Y)):- X = Y.
mirror(tree(L1, R1), tree(L2, R2)):- mirror(L1,R2), mirror(R1, L2).

test_answer0 :-
    mirror(leaf(foo), leaf(foo)),
    write('OK'),
    halt.

test_answer0 :-
    write('Wrong answer!'),
    halt.

test_answer1 :-
    mirror(tree(leaf(foo), leaf(bar)), tree(leaf(bar), leaf(foo))),
    write('OK'),
    halt.

test_answer1 :-
    write('Wrong answer!'),
    halt.

test_answer2 :-
    mirror(tree(tree(leaf(1),  leaf(2)),  leaf(4)), T),
    write(T),
    halt.

test_answer2 :-
    write('Wrong answer!'),
    halt.


test_answer3 :-
    mirror(tree(tree(leaf(1),  leaf(2)),  tree(leaf(3), leaf(4))), T),
    write(T),
    halt.

test_answer3 :-
    write('Wrong answer!'),
    halt.

% Here we test that a single answer is found.

test_answer4 :-
    findall(T, mirror(tree(leaf(121),leaf(367)), T), Results),
    foreach(member(X,Results), (write(X), nl)).

test_answer4 :- write('Wrong answer!'),
    halt.

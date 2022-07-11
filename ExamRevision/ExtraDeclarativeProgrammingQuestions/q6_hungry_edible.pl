eats(alice, X) :- hungry(alice), edible(X), \+ fast_food(X).
eats(bob, X) :- hungry(bob), edible(X).

edible(fries).
edible(salad).
fast_food(fries).

hungry(bob).
hungry(alice).

test_answer :- eats(bob, fries),
               eats(bob, salad),
               eats(alice, salad),
               write('OK').

test_answer :- write('Wrong answer!').

test_answer1 :- eats(alice, fries),
               write('Wrong answer!').

test_answer1 :- write('OK').
